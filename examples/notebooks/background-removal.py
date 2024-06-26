import marimo

__generated_with = "0.3.12"
app = marimo.App(width="medium")


@app.cell
def __():
    import os
    import json
    import base64
    import marimo as mo
    from substrate import (
        Substrate,
        GenerateImage,
        RemoveBackground,
        InpaintImage,
        EraseImage,
        UpscaleImage,
        sb,
    )

    api_key = os.environ.get("SUBSTRATE_API_KEY")
    api_key = api_key or "YOUR_API_KEY"
    substrate = Substrate(
        api_key=api_key,
    )
    return (
        EraseImage,
        GenerateImage,
        InpaintImage,
        RemoveBackground,
        Substrate,
        UpscaleImage,
        api_key,
        base64,
        json,
        mo,
        os,
        sb,
        substrate,
    )


@app.cell
def __(mo):
    prompt = mo.ui.text(
        placeholder="prompt",
        value="a dark red chesterfield leather wing chair in a dark majestic room, pillars, celestial galaxy wallpaper",
        full_width=True,
    ).form()
    prompt
    return prompt,


@app.cell
def __(EraseImage, GenerateImage, InpaintImage, RemoveBackground, prompt):
    image = GenerateImage(
        prompt=prompt.value,
    )
    fg = RemoveBackground(image_uri=image.future.image_uri)
    mask = RemoveBackground(
        image_uri=image.future.image_uri,
        return_mask=True,
    )
    bg = EraseImage(
        image_uri=image.future.image_uri,
        mask_image_uri=mask.future.image_uri,
    )
    bg_prompt = "empty dark majestic room, celestial galaxy wallpaper, high resolution AD"
    inpaint = InpaintImage(image_uri=bg.future.image_uri, prompt=bg_prompt)
    return bg, bg_prompt, fg, image, inpaint, mask


@app.cell
def __(bg, fg, image, inpaint, mask, mo, substrate, upscale):
    viz = substrate.visualize(image, fg, mask, bg, inpaint, upscale)
    mo.md(f"[viz]({viz})")
    return viz,


@app.cell
def __(bg, fg, image, inpaint, mask, mo, substrate, upscale):
    res = substrate.run(image, fg, mask, bg, inpaint, upscale)
    print(res)
    mo.tree(res.json)
    return res,


@app.cell
def __(bg, fg, image, inpaint, mask, mo, res):
    mo.carousel(
        items=[
            mo.vstack(
                [
                    mo.image(src=res.get(image).image_uri),
                ]
            ),
            mo.vstack(
                [
                    mo.image(src=res.get(fg).image_uri),
                ]
            ),
            mo.vstack(
                [
                    mo.image(src=res.get(mask).image_uri),
                ]
            ),
            mo.vstack(
                [
                    mo.image(src=res.get(bg).image_uri),
                ]
            ),
            mo.vstack(
                [
                    mo.image(src=res.get(inpaint).image_uri),
                ]
            ),
        ]
    )
    return


if __name__ == "__main__":
    app.run()
