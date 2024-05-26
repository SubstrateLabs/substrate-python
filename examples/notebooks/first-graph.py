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
    from substrate import Substrate, GenerateTextVision, StableDiffusionXLControlNet, GenerateText, sb

    substrate = Substrate(api_key=api_key)
    return (
        GenerateText,
        GenerateTextVision,
        StableDiffusionXLControlNet,
        Substrate,
        sb,
        substrate,
    )


@app.cell
def __(GenerateTextVision, StableDiffusionXLControlNet, sb, substrate):
    caption = GenerateTextVision(
      prompt="generate a short caption for this image, including color and style details",
      image_uris=["https://guides.substrate.run/hokusai.jpeg"],
    )
    styles = [
      "futuristic supercell spiral cloud with glowing core over turbulent ocean",
      "cityscape skyline background",
      "cinematic sunset bokeh",
    ]
    images = [
      StableDiffusionXLControlNet(
        prompt=sb.concat("photo of ", style, " in the style of: ", caption.future.text),
        image_uri="https://guides.substrate.run/hokusai.jpeg",
        control_method="edge",
        store="hosted",
        num_images=1,
      ) for style in styles]

    result = substrate.run(caption, *images)
    return caption, images, result, styles


@app.cell
def __(mo, result):
    mo.tree(result.api_response.json)
    return


@app.cell
def __(caption, images, mo, substrate):
    viz_url = substrate.visualize(caption, *images)
    mo.md(f"[Visualize the graph]({viz_url})")
    return viz_url,


if __name__ == "__main__":
    app.run()
