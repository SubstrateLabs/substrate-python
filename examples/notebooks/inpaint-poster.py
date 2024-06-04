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
        MultiGenerativeEditImage,
        StableDiffusionXLInpaint,
        UpscaleImage,
        RunPython,
    )

    substrate = Substrate(api_key=api_key)
    return (
        MultiGenerativeEditImage,
        RemoveBackground,
        RunPython,
        StableDiffusionXLInpaint,
        Substrate,
        UpscaleImage,
        substrate,
    )


@app.cell
def __(RemoveBackground, RunPython, StableDiffusionXLInpaint, substrate):
    original_image = "https://media.substrate.run/spc-tw.png"
    mask = RemoveBackground(
        image_uri=original_image,
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
    edit = StableDiffusionXLInpaint(
        image_uri="https://media.substrate.run/spc-tw.png",
        mask_image_uri=crop.future.output["image"],
        strength=0.92,
        prompt="retro computer with black and red smoke and flames billowing out of the screen, high resolution poster",
        negative_prompt="rainbow, paint",
        store="hosted",
        num_images=5,
    )
    res = substrate.run(mask, crop, edit)
    return crop, edit, mask, original_image, res


@app.cell
def __(crop, mask, mo, original_image, res):
    mo.hstack(
        [
            mo.image(original_image),
            mo.image(res.get(mask).image_uri),
            mo.image(res.get(crop).output["image"]),
        ]
    )
    return


@app.cell
def __(edit, mo, res):
    mo.hstack([
        mo.image(res.get(edit).outputs[0].image_uri),
        mo.image(res.get(edit).outputs[1].image_uri),
        mo.image(res.get(edit).outputs[2].image_uri),
        mo.image(res.get(edit).outputs[3].image_uri),
        mo.image(res.get(edit).outputs[4].image_uri),
    ])
    return


@app.cell
def __(edit, mo, res):
    mo.hstack([
        res.get(edit).outputs[0].seed,
        res.get(edit).outputs[1].seed,
        res.get(edit).outputs[2].seed,
        res.get(edit).outputs[3].seed,
    ])
    return


if __name__ == "__main__":
    app.run()
