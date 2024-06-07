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
        UpscaleImage,
    )

    s = Substrate(api_key=api_key)
    return (
        RemoveBackground,
        StableDiffusionXLControlNet,
        Substrate,
        UpscaleImage,
        s,
    )


@app.cell
def __(RemoveBackground, StableDiffusionXLControlNet, s):
    num_images = 2
    mask = RemoveBackground(image_uri="https://media.substrate.run/logo-sq.png", return_mask=True)
    controlnet = StableDiffusionXLControlNet(
        image_uri=mask.future.image_uri,
        control_method="illusion",
        conditioning_scale=1.0,
        prompt="street view futuristic solarpunk city of atlantis",
        num_images=num_images,
    )
    res = s.run(mask, controlnet)
    return controlnet, mask, num_images, res


@app.cell
def __(controlnet, mo, num_images, res):
    mo.hstack([mo.image(res.get(controlnet).outputs[i].image_uri) for i in list(range(num_images))])
    return


@app.cell
def __(controlnet, mo, num_images, res):
    mo.hstack([mo.download(res.get(controlnet).outputs[i].image_uri) for i in list(range(num_images))])
    return


if __name__ == "__main__":
    app.run()
