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
    from substrate import Substrate, GenerateText,GenerateImage, sb

    substrate = Substrate(api_key=api_key)
    return GenerateImage, GenerateText, Substrate, sb, substrate


@app.cell
def __(GenerateImage, GenerateText, sb, substrate):
    story = GenerateText(prompt="tell me a story")
    scene = GenerateText(
      prompt="a short detailed descriptions of a mythical forest creature: ",
    )

    styles = ["woodblock printed", "art nouveau poster"]

    images = [
        GenerateImage(
            prompt=sb.concat("render in a ", style, " style: ", scene.future.text),
            store="hosted") for style in styles]

    result = substrate.run(scene, *images)
    return images, result, scene, story, styles


@app.cell
def __(mo, result):
    mo.tree(result.api_response.json)
    return


@app.cell
def __(images, mo, scene, substrate):
    viz_url = substrate.visualize(scene, *images)
    mo.md(f"[Visualize the graph]({viz_url})")
    return viz_url,


if __name__ == "__main__":
    app.run()
