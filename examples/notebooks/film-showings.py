import marimo

__generated_with = "0.3.12"
app = marimo.App(width="full")


@app.cell(hide_code=True)
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
    from datetime import datetime, timedelta

    today = datetime.today()
    tomorrow = today + timedelta(days=1)
    today_str = today.strftime("%Y-%m-%d")
    tomorrow_str = tomorrow.strftime("%Y-%m-%d")
    return datetime, timedelta, today, today_str, tomorrow, tomorrow_str


@app.cell
def __(today_str, tomorrow_str):
    import requests, re
    from bs4 import BeautifulSoup

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
        pattern,
        pattern_re,
        re,
        requests,
        response,
        soup,
        today_el,
        tomorrow_el,
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


    class Film(BaseModel):
        title: str = Field(..., description="The film's title")
        url: str = Field(..., description="The film's url from the top of the text")
        description: str = Field(..., description="A short summary of the film including genre, director, and year.")
        showtimes: list[str] = Field(..., description="List of showtimes for the film.")


    for url in urls[:5]:
        md = RunPython(
            input={
                "url": url,
            },
            code="""import httpx
    from bs4 import BeautifulSoup
    client = httpx.AsyncClient()
    url = SB_IN['url']
    print(url)
    res = await client.get(url)
    await client.aclose()
    soup = BeautifulSoup(res.text, 'html.parser')
    text = ' '.join([l.strip() for l in soup.text.splitlines() if len(l.strip()) > 0])
    print(text)
    """,
            pip_install=["httpx", "beautifulsoup4"],
        )

        mds.append(md)

        json = GenerateJSON(
            prompt=sb.concat(
                "Summarize the following markdown about a film playing at Metrograph Theater. Do not include Now Playing in the title.\n ",
                md.future.stdout,
            ),
            json_schema=Film.model_json_schema(),
            node="Llama3Instruct8B",
        )
        summaries.append(json)

    markdown = GenerateText(
        prompt=sb.concat(
            "Generate markdown summarizing the following movies. Include title in brackets followed by the url of the film in parentheses, e.g. [title](url). Do not mix up urls. Include a very concise one sentence description. Do not include the theater where the film is playing. Include showtimes. Today is the earliest date that appears, replace the appropriate dates with TODAY and TOMORROW. Do not include preamble before the markdown. Categorize the movies into a few genres.\n",
            *[sb.jq(s.future.json_object, "@json") for s in summaries],
        ),
        node="Llama3Instruct70B",
    )
    res = substrate.run(*summaries, *mds, markdown)
    return Film, json, markdown, md, mds, res, summaries, url


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
