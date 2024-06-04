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
def __():
    from substrate import (
        Substrate,
        StableDiffusionXLControlNet,
        GenerativeEditImage,
        MultiGenerativeEditImage,
        UpscaleImage,
        RemoveBackground,
        RunPython,
    )
    return (
        GenerativeEditImage,
        MultiGenerativeEditImage,
        RemoveBackground,
        RunPython,
        StableDiffusionXLControlNet,
        Substrate,
        UpscaleImage,
    )


@app.cell
def __(Substrate, api_key):
    substrate = Substrate(api_key=api_key)
    return substrate,


@app.cell
def __(
    MultiGenerativeEditImage,
    RemoveBackground,
    RunPython,
    StableDiffusionXLControlNet,
    substrate,
):
    # original = "https://blog.substrate.run/launch-image.png"
    original = "https://media.substrate.run/spc-tw.png"
    controlnet = StableDiffusionXLControlNet(
        image_uri=original,
        control_method="edge",
        prompt="neon lights, retro futuristic 80s club",
        conditioning_scale=1.0,
        num_images=1,
    )
    mask = RemoveBackground(
        image_uri=original,
        return_mask=True,
        store="hosted",
    )
    crop = RunPython(
        input={
            "image": mask.future.image_uri,
        },
        pip_install=["requests", "pillow"],
        code="""# get the bottom left portion of the mask
    from PIL import Image
    from io import BytesIO
    import base64, requests
    response = requests.get(SB_IN["image"])
    img = Image.open(BytesIO(response.content))
    full = 800
    section = 550
    bg = Image.new('RGB', (full, full), (0, 0, 0))
    cropped = img.crop((0, full - section, section, full))
    bg.paste(cropped, (0, full - section))
    buffer = BytesIO()
    bg.save(buffer, format="jpeg")
    b64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
    SB_OUT["image"] = f"data:image/jpeg;base64,{b64}"
    """,
    )
    num_images = 3
    edit = MultiGenerativeEditImage(
        image_uri=controlnet.future.outputs[0].image_uri,
        mask_image_uri=crop.future.output["image"],
        prompt="bright white mirrored metallic water surface high resolution CG render",
        num_images=num_images,
    )
    res = substrate.run(controlnet, mask, crop, edit)
    return controlnet, crop, edit, mask, num_images, original, res


@app.cell
def __(crop, mo, res):
    mo.download(res.get(crop).output["image"])
    return


@app.cell
def __(mo, res):
    mo.tree(res.json)
    return


@app.cell
def __(edit, mo, num_images, res):
    mo.hstack(
        [
            mo.image(res.get(edit).outputs[i].image_uri)
            for i in list(range(num_images))
        ]
    )
    return


@app.cell
def __(edit, mo, num_images, res):
    mo.hstack(
        [
            mo.download(res.get(edit).outputs[i].image_uri)
            for i in list(range(num_images))
        ]
    )
    return


if __name__ == "__main__":
    app.run()
