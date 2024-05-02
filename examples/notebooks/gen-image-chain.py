import marimo

__generated_with = "0.3.12"
app = marimo.App(width="medium")


@app.cell
def __():
    import os
    import json
    import base64
    import marimo as mo
    import substrate as sb

    api_key = os.environ.get("SUBSTRATE_API_KEY")
    api_key = api_key or "YOUR_API_KEY"
    substrate = sb.Substrate(
        api_key=api_key,
        backend="v1",
    )
    return api_key, base64, json, mo, os, sb, substrate


@app.cell
def __(mo):
    prompt = mo.ui.text(
        placeholder="prompt",
        value="A dragon in a forest",
        full_width=True,
    ).form()
    prompt
    return prompt,


@app.cell
def __(prompt, sb):
    image = sb.GenerateImage(
        {
            "prompt": prompt.value,
        }
    )
    rmbg = sb.RemoveBackground({"image_uri": image.future.image_uri})
    rmbg_mask = sb.RemoveBackground(
        {
            "image_uri": image.future.image_uri,
            "return_mask": True,
        }
    )
    bg = sb.FillMask(
        {
            "image_uri": image.future.image_uri,
            "mask_image_uri": rmbg_mask.future.image_uri,
        }
    )
    upscale = sb.UpscaleImage({"image_uri": bg.future.image_uri})
    return bg, image, rmbg, rmbg_mask, upscale


@app.cell
def __(bg, image, mo, rmbg, rmbg_mask, substrate, upscale):
    res = substrate.run(image, rmbg, rmbg_mask, bg, upscale)
    viz = substrate.visualize(image, rmbg, rmbg_mask, bg, upscale)
    mo.md(f"[visualize]({viz})")
    return res, viz


@app.cell
def __(bg, image, mo, res, rmbg, rmbg_mask, upscale):
    mo.hstack(
        [
            mo.image(src=res.get(image).image_uri),
            mo.image(src=res.get(rmbg).image_uri),
            mo.image(src=res.get(rmbg_mask).image_uri),
            mo.image(src=res.get(bg).image_uri),
            mo.download(
                data=res.get(upscale).image_uri,
                filename="upscaled.jpeg",
                label="Upscaled background",
            ),
        ]
    )
    return


if __name__ == "__main__":
    app.run()
