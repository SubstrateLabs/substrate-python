import marimo

__generated_with = "0.3.12"
app = marimo.App(width="medium")


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
    # scrape a list of film urls matching a pattern
    import requests
    from bs4 import BeautifulSoup
    import re

    response = requests.get("https://metrograph.com")
    soup = BeautifulSoup(response.text, "html.parser")
    pattern = r"^https://metrograph.com/film/\?vista_film_id="
    pattern_regex = re.compile(pattern)
    film_urls = []
    for anchor in soup.find_all("a", href=True):
        href = anchor["href"]
        if pattern_regex.match(href):
            film_urls.append(href)
    return (
        BeautifulSoup,
        anchor,
        film_urls,
        href,
        pattern,
        pattern_regex,
        re,
        requests,
        response,
        soup,
    )


@app.cell
def __(GenerateJSON, GenerateText, RunPython, film_urls, sb, substrate):
    summaries = []
    mds = []
    for url in film_urls:
        md = RunPython(
            input={
                "url": url,
            },
            code="""import requests
    res = requests.get(f"https://r.jina.ai/{SB_IN['url']}")
    print(res.content)
    """,
            pip_install=["requests"],
        )
        mds.append(md)
        json = GenerateJSON(
            prompt=sb.concat(
                "Summarize the following markdown about a film playing at Metrograph Theater. Do not include Now Playing in the title.\n ",
                md.future.stdout,
            ),
            json_schema={
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "The film's url from the top of the text",
                    },
                    "title": {
                        "type": "string",
                        "description": "The film's title.",
                    },
                    "description": {
                        "type": "string",
                        "description": "A short summary of the film including genre, director, and year.",
                    },
                },
                "required": [
                    "title",
                    "url",
                    "description",
                ],
            },
            node="Llama3Instruct8B",
        )
        summaries.append(json)

    markdown = GenerateText(
        prompt=sb.concat(
            "Generate markdown summarizing the following movies with the title of the movie linking to its url. Do not include preamble before the markdown. Categorize the movies by genre and make sure any similar categories are combined. ",
            *[sb.jq(s.future.json_object, "@json") for s in summaries],
        ),
        node="Llama3Instruct70B",
    )
    res = substrate.run(*summaries, *mds, markdown)
    return json, markdown, md, mds, res, summaries, url


@app.cell
def __():
    # mo.tree(res.json)
    return


@app.cell
def __(markdown, mo, res):
    mo.md(res.get(markdown).text)
    return


if __name__ == "__main__":
    app.run()
