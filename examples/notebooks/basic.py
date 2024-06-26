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


@app.cell
def __(api_key):
    from substrate import Substrate, ComputeText, Box, If, sb

    substrate = Substrate(api_key=api_key)
    return Box, ComputeText, If, Substrate, sb, substrate


@app.cell
def __(Box, ComputeText):
    story = ComputeText(prompt="tell me a story")
    box = Box(value={
        "story": story.future.text
    })
    return box, story


@app.cell
def __(box, story, substrate):
    res = substrate.run(story, box)
    return res,


@app.cell
def __(box, mo, res):
    mo.tree(res.get(box).value)
    return


@app.cell
def __(mo, res, story):
    mo.md(res.get(story).text)
    return


if __name__ == "__main__":
    app.run()
