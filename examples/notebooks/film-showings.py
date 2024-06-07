import marimo

__generated_with = "0.3.12"
app = marimo.App(width="full")


@app.cell
def __(__file__):
    import os
    import sys
    import typing_extensions
    from pathlib import Path
    import marimo as mo
    from substrate import (
        Substrate,
        GenerateJSON,
        GenerateText,
        RunPython,
        sb,
    )

    # add parent dir to sys.path to make 'substrate' importable
    parent_dir = Path(__file__).resolve().parent.parent
    sys.path.insert(0, str(parent_dir))

    api_key = os.environ.get("SUBSTRATE_API_KEY")
    if api_key is None:
        raise EnvironmentError("No SUBSTRATE_API_KEY set")

    substrate = Substrate(api_key=api_key)
    return (
        GenerateJSON,
        GenerateText,
        Path,
        RunPython,
        Substrate,
        api_key,
        mo,
        os,
        parent_dir,
        sb,
        substrate,
        sys,
        typing_extensions,
    )


@app.cell
def __():
    return


@app.cell
def __():
    import requests, re
    from bs4 import BeautifulSoup
    from datetime import datetime, timedelta

    today = datetime.today()
    tomorrow = today + timedelta(days=1)
    today_str = today.strftime("%Y-%m-%d")
    tomorrow_str = tomorrow.strftime("%Y-%m-%d")

    response = requests.get(f"https://metrograph.com/calendar")
    soup = BeautifulSoup(response.text, "html.parser")
    pattern = r"^/film/\?vista_film_id="
    pattern_re = re.compile(pattern)
    urls = []
    today_el = soup.find(id=f"calendar-list-day-{today_str}")
    tomorrow_el = soup.find(id=f"calendar-list-day-{tomorrow_str}")
    for anchor in today_el.find_all("a", href=True):
        if pattern_re.match(anchor["href"]):
            urls.append(f"https://metrograph.com{anchor['href']}")
    for anchor in tomorrow_el.find_all("a", href=True):
        if pattern_re.match(anchor["href"]):
            urls.append(f"https://metrograph.com{anchor['href']}")
    urls = list(set(urls))
    return (
        BeautifulSoup,
        anchor,
        datetime,
        pattern,
        pattern_re,
        re,
        requests,
        response,
        soup,
        timedelta,
        today,
        today_el,
        today_str,
        tomorrow,
        tomorrow_el,
        tomorrow_str,
        urls,
    )


@app.cell
def __(mo, urls):
    mo.tree(urls)
    return


@app.cell
def __():
    from pydantic import BaseModel, Field
    return BaseModel, Field


@app.cell
def __(
    BaseModel,
    Field,
    GenerateJSON,
    GenerateText,
    RunPython,
    sb,
    substrate,
    urls,
):
    summaries = []
    mds = []
    import json


    class Film(BaseModel):
        title: str = Field(..., description="The film's title")
        url: str = Field(..., description="The film's url from the top of the text")
        description: str = Field(..., description="A short summary of the film including genre, director, and year.")
        showtimes: list[str] = Field(..., description="List of showtimes for the film.")


    for url in urls[:1]:
        md = RunPython(
            input={
                "url": url,
            },
            code="""import requests
    from bs4 import BeautifulSoup
    from markdownify import markdownify
    url = SB_IN['url']
    print(url)
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    SB_OUT['markdown'] = markdownify(str(soup))
    """,
            pip_install=["requests", "beautifulsoup4", "markdownify"],
        )

        mds.append(md)

        summary = GenerateJSON(
            prompt=sb.concat(
                "Summarize the following markdown about a film playing at local theater, generating JSON following the schema below\n ",
                md.future.output["markdown"],
            ),
            json_schema=Film.model_json_schema(),
            node="Llama3Instruct8B",
        )
        summaries.append(summary)

    markdown = GenerateText(
        prompt=sb.concat(
            "Generate markdown summarizing the following movies. Include title in brackets followed by the url of the film in parentheses, e.g. [title](url). Do not mix up urls. Include a very concise one sentence description. Do not include the theater where the film is playing. Include showtimes. Today is the earliest date that appears, replace the appropriate dates with TODAY and TOMORROW. Do not include preamble before the markdown. Categorize the movies into a few genres.\n",
            *[sb.jq(s.future.json_object, "@json") for s in summaries],
        ),
        node="Llama3Instruct70B",
    )
    res = substrate.run(*summaries, *mds, markdown)
    return Film, json, markdown, md, mds, res, summaries, summary, url


@app.cell
def __(mo, res):
    mo.tree(res.json)
    return


@app.cell
def __(markdown, mo, res):
    mo.md(res.get(markdown).text)
    return


@app.cell
def __(markdown, res):
    print(res.get(markdown).text)
    return


if __name__ == "__main__":
    app.run()
