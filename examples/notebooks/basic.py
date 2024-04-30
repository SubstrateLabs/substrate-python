import marimo

__generated_with = "0.3.12"
app = marimo.App()


@app.cell
def __():
    import os
    import json
    import base64

    import marimo as mo

    api_key = os.environ.get("SUBSTRATE_API_KEY")
    api_key = api_key or "YOUR_API_KEY"
    api_key
    return api_key, base64, json, mo, os


@app.cell(hide_code=True)
def __(mo):
    mo.md("Initialize the Substrate client.")
    return


@app.cell
def __(api_key):
    from substrate import Substrate, GenerateText, sb

    substrate = Substrate(api_key=api_key)
    return GenerateText, Substrate, sb, substrate


@app.cell(hide_code=True)
def __(mo):
    mo.md("Generate a story using the [`GenerateText`](https://www.substrate.run/nodes#GenerateText) node.")
    return


@app.cell
def __(GenerateText):
    story = GenerateText({"prompt": "tell me a story"})
    return (story,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        "Summarize the output of the `story` node using another `GenerateText` node. Because `story` has not yet been run, we use `sb.concat` to work with its future output"
    )
    return


@app.cell
def __(GenerateText, sb, story):
    summary = GenerateText({"prompt": sb.concat("summarize this story in one sentence: ", story.future.text)})
    return (summary,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        "Run the graph chaining `story` → `summary`. This is a simple example, but you can easily build arbitrarily complex branching workflows."
    )
    return


@app.cell
def __(story, substrate, summary):
    response = substrate.run(story, summary)
    return (response,)


@app.cell(hide_code=True)
def __(mo):
    mo.md("Get the output of the summary node by passing it to `response.get`.")
    return


@app.cell
def __(mo, response, summary):
    summary_out = response.get(summary)
    mo.md(summary_out.text)
    return (summary_out,)


@app.cell
def __(mo, story, substrate, summary):
    viz_url = substrate.visualize(story, summary)
    mo.md(f"[Visualize the graph]({viz_url})")
    return (viz_url,)


if __name__ == "__main__":
    app.run()
