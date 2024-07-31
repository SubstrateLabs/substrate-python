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
    return api_key, json, mo, os


@app.cell
def __(api_key):
    from substrate import Substrate

    substrate = Substrate(api_key=api_key, base_url="https://api-staging.substrate.run")
    return Substrate, substrate


@app.cell
def __(substrate):
    from substrate import GenerateImage, UpscaleImage, StableVideoDiffusion

    prompt = "aerial shot of rainforest at sunset clouds sun rays"
    image_node = GenerateImage(prompt=prompt)
    upscale_node = UpscaleImage(prompt=prompt, 
                                output_resolution=2048,
                                image_uri=image_node.future.image_uri)
    video_node = StableVideoDiffusion(image_uri=upscale_node.future.image_uri, 
                                      store="hosted", 
                                      motion_bucket_id=20, 
                                      fps=10
    )

    res = substrate.run(video_node)
    return (
        GenerateImage,
        StableVideoDiffusion,
        UpscaleImage,
        image_node,
        prompt,
        res,
        upscale_node,
        video_node,
    )


@app.cell
def __(mo, res, video_node):
    video = res.get(video_node).video_uri
    mo.image(video)
    return video,


@app.cell
def __(mo, res, upscale_node):
    image = res.get(upscale_node).image_uri
    mo.image(image)
    return image,


if __name__ == "__main__":
    app.run()
