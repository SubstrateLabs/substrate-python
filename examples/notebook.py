import marimo

__generated_with = "0.4.1"
app = marimo.App()


@app.cell
def __():
    import os
    import json
    import base64

    import marimo as mo

    api_key = os.environ.get("SUBSTRATE_API_KEY")
    print(api_key)
    return api_key, base64, json, mo, os


@app.cell
def __(api_key):
    from substrate import Substrate

    s = Substrate(api_key=api_key)
    return Substrate, s


@app.cell
def __(s):
    from substrate import StableDiffusionXL

    _node = StableDiffusionXL(
        {
            "prompt": "cinematic film still of a translucent (cybernetic chip data center predatory spiral Conus Conidae shell)1.5, (glowing veins)1.3 (cables going into body, circuits)1.3, extremely detailed, vignette, highly detailed, high budget, bokeh, moody, epic, gorgeous, film grain, grainy",
        }
    ).subscribe()
    _res = s.run(_node, use_requests=True)
    sdxl_out = _node.output(_res)
    print(sdxl_out)
    return StableDiffusionXL, sdxl_out


@app.cell
def __(base64, mo, sdxl_out):
    _bytes = [base64.b64decode(i["image_uri"].removeprefix("data:image/jpeg;base64,")) for i in sdxl_out.outputs]
    mo.hstack([mo.image(src=b) for b in _bytes])
    return


@app.cell
def __(s):
    from substrate import StableDiffusionXLTurbo

    _node = StableDiffusionXLTurbo(
        {
            "prompt": "cinematic film still of a translucent (cybernetic chip data center predatory spiral Conus Conidae shell)1.5, (glowing veins)1.3 (cables going into body, circuits)1.3, extremely detailed, vignette, highly detailed, high budget, bokeh, moody, epic, gorgeous, film grain, grainy",
            "num_images": 1,
            "width": 800,
            "height": 512,
            # "guidance_scale": sdxl_form.value[5],
            # "store": "hosted",
        }
    ).subscribe()
    _res = s.run(_node)
    turbo_out = _node.output(_res)
    print(turbo_out)
    return StableDiffusionXLTurbo, turbo_out


@app.cell
def __(base64, mo, turbo_out):
    _bytes = [base64.b64decode(i["image_uri"].removeprefix("data:image/jpeg;base64,")) for i in turbo_out.outputs]
    mo.hstack([mo.image(src=b) for b in _bytes])
    return


@app.cell
def __(StableDiffusionXLTurbo, s):
    from substrate import StableDiffusionXLLightning

    _node = StableDiffusionXLTurbo(
        {
            "prompt": "cinematic film still of a translucent (cybernetic chip data center predatory spiral Conus Conidae shell)1.5, (glowing veins)1.3 (cables going into body, circuits)1.3, extremely detailed, vignette, highly detailed, high budget, bokeh, moody, epic, gorgeous, film grain, grainy",
            "num_images": 1,
            "width": 800,
            "height": 512,
            # "guidance_scale": sdxl_form.value[5],
            # "store": "hosted",
        }
    ).subscribe()
    _res = s.run(_node)
    lightning_out = _node.output(_res)
    print(lightning_out)
    return StableDiffusionXLLightning, lightning_out


@app.cell
def __(base64, lightning_out, mo):
    _bytes = [base64.b64decode(i["image_uri"].removeprefix("data:image/jpeg;base64,")) for i in lightning_out.outputs]
    mo.hstack([mo.image(src=b) for b in _bytes])
    return


if __name__ == "__main__":
    app.run()
