import marimo

__generated_with = "0.3.12"
app = marimo.App(width="medium")


@app.cell
def __():
    import os
    import json
    import base64
    import marimo as mo
    import substrate as sb

    api_key = os.environ.get("SUBSTRATE_API_KEY")
    api_key = api_key or "YOUR_API_KEY"
    mo.md(f"`{api_key}`")
    return api_key, base64, json, mo, os, sb


@app.cell
def __(api_key, sb):
    substrate = sb.Substrate(
        api_key=api_key,
        backend="v1",
    )
    return substrate,


@app.cell
def __(mo):
    prompt = mo.ui.text(
        placeholder="prompt",
        value="A bowl of fruit",
        full_width=True,
    ).form()
    prompt
    return prompt,


@app.cell
def __(prompt, sb):
    image = sb.GenerateImage(
        {
            "prompt": prompt.value,
        }
    )
    return image,


@app.cell
def __(image, sb):
    rmbg = sb.RemoveBackground({
        "image_uri": image.future.image_uri
    })
    return rmbg,


@app.cell
def __(image, sb):
    upscale = sb.UpscaleImage({
        "image_uri": image.future.image_uri
    })
    return upscale,


@app.cell
def __(image, mo, rmbg, substrate, upscale):
    res = substrate.run(image, rmbg, upscale)
    viz = substrate.visualize(image, rmbg, upscale)
    mo.md(f"[visualize]({viz})")
    return res, viz


@app.cell
def __(image, mo, res):
    image_out = res.get(image)
    mo.image(src=image_out.image_uri)
    return image_out,


@app.cell
def __(mo, res, rmbg):
    rmbg_out = res.get(rmbg)
    mo.image(src=rmbg_out.image_uri)
    return rmbg_out,


@app.cell
def __(mo, res, upscale):
    upscale_out = res.get(upscale)
    mo.download(
        data=upscale_out.image_uri,
        filename="upscaled.jpeg",
    )
    return upscale_out,


if __name__ == "__main__":
    app.run()
