import datetime
import os
import sys
from pathlib import Path
import requests
import time
import json
from xml.etree import ElementTree
from pydantic import BaseModel
from typing import List, Optional
import pendulum
from bs4 import BeautifulSoup
from multiprocessing import Pool

MAX_RETRIES = 5

class NewsItem(BaseModel):
    title: str
    link: str
    description: str
    source_url: str
    source_name: str
    pub_date: str

class NewsItemWithText(NewsItem):
    text: str

def get_ap_news_item_text(news_item: NewsItem, retries: int = 0) -> str:
    print("Getting text for", news_item.title, "attempt number:", retries)
    time.sleep(2)
    response = requests.get(news_item.link)
    text = response.text
    parsed_text = BeautifulSoup(text, "html.parser")
    story_text = parsed_text.find("bsp-story-page")
    if not story_text:
        story_selector = parsed_text.select(".Page-oneColumn")
        if not story_selector:
            story_selector = parsed_text.select(".Page-storyBody")
        try:
            story_text = story_selector[0]
        except IndexError:
            if retries >= MAX_RETRIES:
                print("Failed to get text for", news_item.title, "after", MAX_RETRIES, "retries")
                return ""
            retries += 1
            return get_ap_news_item_text(news_item, retries)
    return story_text.text.strip()

def add_news_item_text(news_item: NewsItem) -> NewsItemWithText:
    news_retrieval_fn = {
        "https://apnews.com": get_ap_news_item_text
    }
    return NewsItemWithText(**news_item.dict(), text=news_retrieval_fn[news_item.source_url](news_item))

def get_items_from_google_news_url(url: str) -> List[NewsItem]:
    gn_response = requests.get("https://news.google.com/rss/search?q=when:24h allinurl:apnews.com")
    gn_text = gn_response.text
    ap_xml = ElementTree.fromstring(gn_text)
    channel = ap_xml[0]
    news_items = channel.findall("item")
    return [NewsItem.parse_obj({
        "title": item.find("title").text,
        "link": item.find("link").text,
        "description": item.find("description").text,
        "source_url": item.find("source").attrib["url"],
        "source_name": item.find("source").text,
        "pub_date": pendulum.from_format(item.find("pubDate").text, "ddd, DD MMM YYYY HH:mm:ss z").isoformat()
    }) for item in news_items]
    return news_items

# add parent dir to sys.path to make 'substrate' importable
parent_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(parent_dir))

api_key = os.environ.get("SUBSTRATE_API_KEY")
if api_key is None:
    raise EnvironmentError("No SUBSTRATE_API_KEY set")

from substrate import Substrate, MultiEmbedText, FindOrCreateVectorStore, DeleteVectorStore

if __name__ == "__main__":
    substrate = Substrate(api_key=api_key, timeout=60 * 5, base_url="https://kube-dev.substrate.run/ray/stable")
    pool = Pool(8)

    ap_news_items = get_items_from_google_news_url("https://news.google.com/rss/search?q=when:24h allinurl:apnews.com")
    ap_news_items_with_text = pool.map(add_news_item_text, ap_news_items)

    old_collection = DeleteVectorStore(
        collection_name= "substrate_news_bot",
        model= "jina-v2"
    )

    collection = FindOrCreateVectorStore(
            collection_name= old_collection.future.collection_name,
            model= old_collection.future.model,
    )

    news_items = MultiEmbedText(
        items=[{"text": item.text, "metadata": {k: v for k, v in item.dict().items() if k != "text"}} for item in ap_news_items_with_text],
        collection_name=collection.future.collection_name,
        embedded_metadata_keys=["title", "link", "description", "source_url", "source_name", "pub_date"],
    )

    res = substrate.run(news_items)
    print(res.json)
