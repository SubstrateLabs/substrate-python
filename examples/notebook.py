import marimo

__generated_with = "0.3.4"
app = marimo.App()


@app.cell
def __():
    import os
    import json

    import marimo as mo

    api_key = os.environ.get("SUBSTRATE_API_KEY")
    print(api_key)
    return api_key, json, mo, os


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
def __(api_key, json, prompt):
    from substrate import Substrate

    s = Substrate(api_key=api_key)
    result = s.run(prompt)
    print(result.api_response.status_code)
    print(json.dumps(result.api_response.json, indent=2))
    return Substrate, result, s


if __name__ == "__main__":
    app.run()
