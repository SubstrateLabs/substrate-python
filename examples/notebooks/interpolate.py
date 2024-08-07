import marimo

__generated_with = "0.6.23"
app = marimo.App()


@app.cell
def __():
    import os
    import json

    import marimo as mo

    api_key = os.environ.get("SUBSTRATE_API_KEY")
    api_key = api_key or "YOUR_API_KEY"
    print(api_key)
    return api_key, json, mo, os


@app.cell
def __(api_key):
    from substrate import Substrate

    substrate = Substrate(api_key=api_key, base_url="https://api.substrate.run")
    return Substrate, substrate


@app.cell
def __(substrate):
    from substrate import GenerateImage, InterpolateFrames, StableDiffusionXLInpaint

    # Generate a base image
    base_image = GenerateImage(prompt="aerial view of ocean waves")

    # Generate variations
    times = [
        "6am sunrise",
        "1pm afternoon bright sun",
        "8pm after sunset",
    ]
    images = []
    for t in times:
        image = StableDiffusionXLInpaint(
            image_uri=base_image.future.image_uri,
            prompt=f"aerial view of rainforest, {t}",
            num_images=1,
            strength=0.9,
        )
        images.append(image)

    # Interpolate from base through variations
    interpolate = InterpolateFrames(
        frame_uris=[
            base_image.future.image_uri,
            images[0].future.outputs[0].image_uri,
            images[1].future.outputs[0].image_uri,
            images[2].future.outputs[0].image_uri,
            base_image.future.image_uri,
        ],
        num_steps=2,
        store="hosted",
        output_format="mp4",
    )
    res = substrate.run(interpolate)
    return (
        GenerateImage,
        InterpolateFrames,
        StableDiffusionXLInpaint,
        base_image,
        image,
        images,
        interpolate,
        res,
        t,
        times,
    )


@app.cell
def __(res):
    print(res.request_id)
    print(res)
    return


@app.cell
def __(interpolate, res):
    print(res.get(interpolate).video_uri)
    return


@app.cell
def __(interpolate, mo, res):
    mo.image(res.get(interpolate).video_uri)
    return


@app.cell
def __(images, mo, res):
    mo.vstack(
        [
            mo.image(res.get(images[0]).outputs[0].image_uri),
            mo.image(res.get(images[1]).outputs[0].image_uri),
            mo.image(res.get(images[2]).outputs[0].image_uri),
            mo.image(res.get(images[3]).outputs[0].image_uri),
        ]
    )
    return


if __name__ == "__main__":
    app.run()
