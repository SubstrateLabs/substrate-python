import marimo

__generated_with = "0.3.12"
app = marimo.App(width="medium")


@app.cell
def __():
    import time

    print(f"time {int(time.time())}")
    return (time,)


@app.cell
def __(__file__):
    import os
    import sys
    import typing_extensions
    from pathlib import Path
    import marimo as mo
    import substrate as ss

    # add parent dir to sys.path to make 'substrate' importable
    parent_dir = Path(__file__).resolve().parent.parent
    sys.path.insert(0, str(parent_dir))

    api_key = os.environ.get("SUBSTRATE_API_KEY")
    if api_key is None:
        raise EnvironmentError("No SUBSTRATE_API_KEY set")

    substrate = ss.Substrate(api_key=api_key)
    return (
        Path,
        api_key,
        mo,
        os,
        parent_dir,
        ss,
        substrate,
        sys,
        typing_extensions,
    )


@app.cell
def __():
    # create = ss.CreateVectorStore(
    #   collection_name="image_prompt_enhancements",
    #   model="jina-v2",
    # );
    # create_res = substrate.run(create)

    # mo.tree(create_res.json)
    return


@app.cell
def __(ss):
    enhancements = [
        "highly detailed",
        "digital painting",
        "ultrafine detailed painting",
        "cell shaded cartoon",
        "concept art",
        "matte",
        "octane render",
        "volumetric lighting",
        "exquisite detail",
        "8k postprocessing",
        "cinematic",
        "sharp focus",
        "wide shot",
        "wide angle",
    ]
    nodes = []
    for e in enhancements:
        embed = ss.EmbedText(
            text=e,
            collection_name="image_prompt_enhancements",
            model="jina-v2",
        )
        nodes.append(embed)
    # embed_res = substrate.run(*nodes)
    # mo.tree(embed_res.json)
    return e, embed, enhancements, nodes


@app.cell
def __(mo, ss, substrate):
    prompt = "a towering spiral seashell in a city the size of a city skyscraper"
    query = ss.QueryVectorStore(
        query_strings=[prompt],
        collection_name="image_prompt_enhancements",
        model="jina-v2",
        include_metadata=True,
        top_k=3,
    )
    image1 = ss.GenerateImage(
        prompt=ss.sb.concat(
            prompt,
            "octane render, volumetric lighting, cinematic, highly detailed, ",
            query.future.results[0][0].metadata["doc"],
        )
    )
    image2 = ss.GenerateImage(
        prompt=ss.sb.concat(
            prompt,
            "cell shaded cartoon, volumetric lighting, cinematic, highly detailed, ",
            query.future.results[0][1].metadata["doc"],
        )
    )
    query_res = substrate.run(query, image1, image2)
    # query_out = query_res.get(query);
    mo.tree(query_res.json)
    return image1, image2, prompt, query, query_res


@app.cell
def __(image1, image2, mo, query_res):
    mo.hstack(
        [
            mo.vstack(
                [
                    mo.image(query_res.get(image1).image_uri),
                    mo.download(query_res.get(image1).image_uri),
                ]
            ),
            mo.vstack(
                [
                    mo.image(query_res.get(image2).image_uri),
                    mo.download(query_res.get(image2).image_uri),
                ]
            ),
        ]
    )
    return


@app.cell
def __():
    # mo.tree(response.json)
    return


if __name__ == "__main__":
    app.run()
