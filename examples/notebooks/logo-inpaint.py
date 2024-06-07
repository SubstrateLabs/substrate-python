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

    # add parent dir to sys.path to make 'substrate' importable
    parent_dir = Path(__file__).resolve().parent.parent
    sys.path.insert(0, str(parent_dir))

    api_key = os.environ.get("SUBSTRATE_API_KEY")
    if api_key is None:
        raise EnvironmentError("No SUBSTRATE_API_KEY set")
    return Path, api_key, mo, os, parent_dir, sys, typing_extensions


@app.cell
def __(api_key):
    from substrate import (
        Substrate,
        RemoveBackground,
        StableDiffusionXLControlNet,
        StableDiffusionXLInpaint,
        GenerativeEditImage,
    )

    s = Substrate(api_key=api_key)
    return (
        GenerativeEditImage,
        RemoveBackground,
        StableDiffusionXLControlNet,
        StableDiffusionXLInpaint,
        Substrate,
        s,
    )


@app.cell
def __(
    RemoveBackground,
    StableDiffusionXLControlNet,
    StableDiffusionXLInpaint,
    mo,
    s,
):
    original = "https://media.substrate.run/logo-sq.png"
    mask = RemoveBackground(image_uri=original, return_mask=True)
    controlnet = StableDiffusionXLControlNet(
        image_uri=original,
        control_method="edge",
        prompt="bright silver disco high contrast",
        conditioning_scale=0.8,
        num_images=1,
    )
    inpaint = StableDiffusionXLInpaint(
        image_uri=controlnet.future.outputs[0].image_uri,
        mask_image_uri=mask.future.image_uri,
        prompt="towers in the futuristic ancient solarpunk city of atlantis",
        num_images=2,
    )
    res = s.run(mask, controlnet, inpaint)
    mo.tree(res.json)
    return controlnet, inpaint, mask, original, res


@app.cell
def __(controlnet, mo, res):
    mo.image(res.get(controlnet).outputs[0].image_uri)
    return


@app.cell
def __(inpaint, mo, res):
    mo.image(res.get(inpaint).outputs[0].image_uri)
    return


@app.cell
def __(inpaint, mo, res):
    mo.image(res.get(inpaint).outputs[1].image_uri)
    return


@app.cell
def __(controlnet, inpaint, mo, res):
    mo.hstack([
        mo.download(res.get(controlnet).outputs[0].image_uri),
        mo.download(res.get(inpaint).outputs[0].image_uri),
        mo.download(res.get(inpaint).outputs[1].image_uri),
    ])
    return


if __name__ == "__main__":
    app.run()
