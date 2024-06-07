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
        StableDiffusionXLControlNet,
        StableDiffusionXLInpaint,
        GenerativeEditImage,
        GenerateTextVision,
        GenerateText,
        sb,
    )

    substrate = Substrate(api_key=api_key)
    return (
        GenerateText,
        GenerateTextVision,
        GenerativeEditImage,
        StableDiffusionXLControlNet,
        StableDiffusionXLInpaint,
        Substrate,
        sb,
        substrate,
    )


@app.cell
def __(
    GenerateText,
    GenerateTextVision,
    StableDiffusionXLInpaint,
    sb,
    substrate,
):
    styles = ["sunlit onsen style tokyo office", "80s disco style berlin office at night"]
    images = [
        StableDiffusionXLInpaint(
            image_uri="https://media.substrate.run/office.jpg",
            # control_method="depth",
            strength=0.75,
            prompt=s,
            num_images=1,
        )
        for s in styles
    ]
    descriptions = [
        GenerateTextVision(
            prompt="Describe the interesting interior decor touches in this image",
            # image_uris=[i.future.image_uri],
            image_uris=[i.future.outputs[0].image_uri],
        )
        for i in images
    ]
    summaries = [
        GenerateText(
            prompt=sb.concat(
                "Summarize the 2 most interesting details in one sentence, be concise: ",
                d.future.text,
            ),
        )
        for d in descriptions
    ]
    res = substrate.run(*images, *descriptions, *summaries)
    return descriptions, images, res, styles, summaries


@app.cell
def __(mo, res):
    mo.tree(res.json)
    return


@app.cell
def __(mo, original_image):
    mo.image(original_image)
    return


@app.cell
def __(images, mo, res, summaries):
    mo.vstack(
        [
            mo.vstack(
                [
                    mo.image(res.get(images[0]).image_uri),
                    mo.md(res.get(summaries[0]).text),
                ]
            ),
            mo.vstack(
                [
                    mo.image(res.get(images[1]).image_uri),
                    mo.md(res.get(summaries[1]).text),
                ]
            ),
        ]
    )
    return


@app.cell
def __(images, mo, res, summaries):
    mo.vstack(
        [
            mo.vstack(
                [
                    mo.image(res.get(images[0]).outputs[0].image_uri),
                    mo.md(res.get(summaries[0]).text),
                ]
            ),
            mo.vstack(
                [
                    mo.image(res.get(images[1]).outputs[0].image_uri),
                    mo.md(res.get(summaries[1]).text),
                ]
            ),
        ]
    )
    return


@app.cell
def __(images, mo, res):
    mo.hstack(
        [
            mo.download(res.get(images[0]).image_uri),
            mo.download(res.get(images[1]).image_uri),
        ]
    )
    return


@app.cell
def __(images, mo, res):
    mo.hstack(
        [
            mo.download(res.get(images[0]).outputs[0].image_uri),
            mo.download(res.get(images[1]).outputs[0].image_uri),
        ]
    )
    return


if __name__ == "__main__":
    app.run()
