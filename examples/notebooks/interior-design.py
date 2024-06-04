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
        GenerateTextVision,
        GenerateText,
        sb,
    )

    substrate = Substrate(api_key=api_key)
    return (
        GenerateText,
        GenerateTextVision,
        RemoveBackground,
        StableDiffusionXLControlNet,
        Substrate,
        UpscaleImage,
        sb,
        substrate,
    )


@app.cell
def __(
    GenerateText,
    GenerateTextVision,
    StableDiffusionXLControlNet,
    sb,
    substrate,
):
    num_frames = 8
    original_image = "https://media.substrate.run/office.jpg"
    times = ["5am in tokyo", "10am in paris", "6pm in london", "10pm in berlin"]
    images = [
        StableDiffusionXLControlNet(
            image_uri=original_image,
            control_method="depth",
            # conditioning_scale=1,
            prompt=sb.concat("cozy office at ", t),
            num_images=num_frames,
        )
        for t in times
    ]
    captions = [
        GenerateTextVision(
            prompt="Describe the interesting interior decor touches in this image",
            image_uris=[i.future.outputs[0].image_uri],
        )
        for i in images
    ]
    summaries = [
        GenerateText(
            prompt=sb.concat(
                "Summarize the 2 most interesting details in one sentence, be concise: ",
                c.future.text,
            ),
        )
        for c in captions
    ]
    res = substrate.run(*images, *captions, *summaries)
    return (
        captions,
        images,
        num_frames,
        original_image,
        res,
        summaries,
        times,
    )


@app.cell
def __(mo, original_image):
    mo.image(original_image)
    return


@app.cell
def __(images, mo, res, summaries):
    mo.hstack(
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
def __(images, mo, res, summaries):
    mo.hstack(
        [
            mo.vstack(
                [
                    mo.image(res.get(images[2]).outputs[0].image_uri),
                    mo.md(res.get(summaries[2]).text),
                ]
            ),
            mo.vstack(
                [
                    mo.image(res.get(images[3]).outputs[0].image_uri),
                    mo.md(res.get(summaries[3]).text),
                ]
            ),
        ]
    )
    return


@app.cell
def __(images, mo, res):
    mo.hstack(
        [
            mo.download(res.get(images[0]).outputs[0].image_uri),
            mo.download(res.get(images[1]).outputs[0].image_uri),
            mo.download(res.get(images[2]).outputs[0].image_uri),
            mo.download(res.get(images[3]).outputs[0].image_uri),
        ]
    )
    return


if __name__ == "__main__":
    app.run()
