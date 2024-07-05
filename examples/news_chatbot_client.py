import os
import sys
from pathlib import Path
import requests
import json

from substrate.nodes import ComputeText


# add parent dir to sys.path to make 'substrate' importable
parent_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(parent_dir))

api_key = os.environ.get("SUBSTRATE_API_KEY")
if api_key is None:
    raise EnvironmentError("No SUBSTRATE_API_KEY set")

from substrate import Substrate, FindOrCreateVectorStore, QueryVectorStore, BatchComputeText, sb

substrate = Substrate(api_key=api_key, timeout=60 * 5, base_url="https://kube-dev.substrate.run/ray/stable")

# previous_response = ""
while "still running chat":
    prompt_text = input("Please ask me a question: ")

    collection = FindOrCreateVectorStore(
            collection_name= "substrate_news_bot",
            model= "jina-v2"
    )

    relevant_news_items = QueryVectorStore(
        collection_name= collection.future.collection_name,
        model=collection.future.model,
        query_strings=[prompt_text],
        top_k=5,
        include_metadata=True,
    )

    generated_text = ComputeText(
            prompt=sb.concat("""
    You are a helpful and expert analyst of world events.  A user is going to ask you a question about
    recent events, and your assistant will provide you with relevant news articles.  Please use
    the following articles to summarize the key points about the user's question.  The user is looking for a high-level overview of the following news items:
        """,
            "*** NEWS ARTICLES ***\n",
            sb.concat(sb.jq(relevant_news_items.future.results, '.[0].[0].metadata.doc'), "\n"),
            # "*** PREVIOUS RESPONSE ***\n"
            # "If you've provided a response before, please use it to inform your next answer, unless",
            # " the new prompt is not related:\n",
            # previous_response,
            "*** USER QUESTION: ***\n",
            "The user's question is:\n",
            prompt_text
        )
    )
    res = substrate.stream(generated_text)
    # previous_response = ""
    for item in res.iter():
        if item.data["object"] == "node.delta":
            out = item.data.get("data", {}).get("text", "")
            # previous_response += out
            sys.stdout.write(out)
    sys.stdout.write("\n")
