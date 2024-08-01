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
    from substrate import GenerateImage, UpscaleImage, StableVideoDiffusion

    prompt = "aerial shot of desert at sunset under clouds"
    image_node = GenerateImage(
        prompt=prompt,
        seed=888,
    )
    video_node = StableVideoDiffusion(
        image_uri=image_node.future.image_uri, store="hosted", motion_bucket_id=20, fps=10
    )

    res = substrate.run(video_node)
    return (
        GenerateImage,
        StableVideoDiffusion,
        UpscaleImage,
        image_node,
        prompt,
        res,
        video_node,
    )


@app.cell
def __(res):
    print(res.request_id)
    print(res)
    return


@app.cell
def __(res, video_node):
    video = res.get(video_node).video_uri
    print(video)
    return video,


@app.cell
def __(mo, video):
    mo.image(video)
    return


if __name__ == "__main__":
    app.run()
