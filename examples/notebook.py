import marimo

__generated_with = "0.3.3"
app = marimo.App()


@app.cell
def __():
    import os

    import marimo as mo

    api_key = os.environ.get("SUBSTRATE_API_KEY")
    return api_key, mo, os


@app.cell
def __():
    from substrate import GenerateText

    prompt = GenerateText(
        {
            "prompt": "Generate a short description that a painter could use to accurately paint a picture of a city scene, including adjectives that would enhance the quality of the end result. Only return the description, no additional text."
        }
    ).subscribe()
    return GenerateText, prompt


@app.cell
def __(prompt):
    from substrate import GenerateImage

    image = GenerateImage({"prompt": prompt.future.text}).subscribe()
    return GenerateImage, image


@app.cell
async def __(api_key, image, prompt):
    from substrate import AsyncSubstrate

    s = AsyncSubstrate(api_key=api_key)
    result = await s.run(prompt, image)
    return AsyncSubstrate, result, s


@app.cell
def __(image, mo, result):
    import base64

    image_data = image.output(result).image_uri
    mo.image(src=base64.b64decode(image_data))
    return base64, image_data


@app.cell
def __(mo, prompt, result):
    mo.md(prompt.output(result).text)
    return


if __name__ == "__main__":
    app.run()
