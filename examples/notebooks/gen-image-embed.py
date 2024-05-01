import marimo

__generated_with = "0.3.12"
app = marimo.App(width="medium")


@app.cell
def __():
    import os
    import json
    import string
    import random
    import base64
    import marimo as mo
    import substrate as sb

    api_key = os.environ.get("SUBSTRATE_API_KEY")
    api_key = api_key or "YOUR_API_KEY"
    mo.md(f"`{api_key}`")
    characters = string.ascii_letters
    random_string = "".join(random.choice(characters) for i in range(3))
    collection_name = f"image_test_a3"
    collection_name
    return (
        api_key,
        base64,
        characters,
        collection_name,
        json,
        mo,
        os,
        random,
        random_string,
        sb,
        string,
    )


@app.cell
def __(api_key, sb):
    substrate = sb.Substrate(
        api_key=api_key,
        backend="v1",
    )
    return substrate,


@app.cell
def __(collection_name, mo, sb, substrate):
    # create the vector store
    create_vstore = sb.CreateVectorStore(
        {"model": "clip", "collection_name": collection_name}
    )
    create_res = substrate.run(create_vstore)
    mo.tree(create_res.json)
    return create_res, create_vstore


@app.cell
def __(mo):
    prompt = mo.ui.text(
        placeholder="prompt",
        value="A bowl of fruit",
        full_width=True,
    ).form()
    prompt
    return prompt,


@app.cell
def __(collection_name, prompt, sb):
    image = sb.GenerateImage(
        {
            "prompt": prompt.value,
        }
    )
    embed_prompt = sb.EmbedText(
        {
            "text": prompt.value,
            "collection_name": collection_name,
        }
    )
    embed = sb.EmbedImage(
        {
            "image_uri": image.future.image_uri,
            "collection_name": collection_name,
        }
    )
    return embed, embed_prompt, image


@app.cell
def __(embed, embed_prompt, image, mo, substrate):
    res = substrate.run(image, embed, embed_prompt)
    mo.tree(res.json)
    return res,


@app.cell
def __(embed_prompt, res):
    prompt_doc_id = res.get(embed_prompt).embedding.doc_id
    print(prompt_doc_id)
    return prompt_doc_id,


@app.cell
def __(embed, res):
    image1_doc_id = res.get(embed).embedding.doc_id
    print(image1_doc_id)
    return image1_doc_id,


@app.cell
def __(mo):
    prompt2 = mo.ui.text(
        placeholder="prompt",
        value="A bowl of chocolate",
        full_width=True,
    ).form()
    prompt2
    return prompt2,


@app.cell
def __(collection_name, prompt2, sb):
    image2 = sb.GenerateImage(
        {
            "prompt": prompt2.value,
        }
    )
    embed2 = sb.EmbedImage(
        {
            "image_uri": image2.future.image_uri,
            "collection_name": collection_name,
        }
    )
    return embed2, image2


@app.cell
def __(embed2, image2, mo, substrate):
    res2 = substrate.run(image2, embed2)
    mo.tree(res2.json)
    return res2,


@app.cell
def __(embed2, res2):
    image2_doc_id = res2.get(embed2).embedding.doc_id
    print(image2_doc_id)
    return image2_doc_id,


@app.cell
def __(collection_name, image, res, sb):
    query = sb.QueryVectorStore(
        {
            "model": "clip",
            "collection_name": collection_name,
            "query_image_uris": [res.get(image).image_uri],
            "top_k": 100,
            "ef_search": 64,
            # "query_strings": [prompt.value],
        }
    )
    return query,


@app.cell
def __(query, substrate):
    query_res = substrate.run(query)
    return query_res,


@app.cell
def __(query, query_res):
    results = query_res.get(query).results
    return results,


@app.cell
def __(mo, results):
    mo.tree(results)
    return


@app.cell
def __(image2_doc_id, mo, results):
    image2_distance = None
    for r in results[0]:
        if r.id == image2_doc_id:
            image2_distance = r.distance

    mo.tree(
        {
            "image2_distance": image2_distance,
        }
    )
    return image2_distance, r


@app.cell
def __(image, image2, image2_distance, mo, res, res2):
    mo.hstack(
        [
            mo.vstack(
                [
                    mo.image(src=res.get(image).image_uri),
                ]
            ),
            mo.vstack(
                [
                    mo.image(src=res2.get(image2).image_uri),
                    mo.md(f"distance: {image2_distance}"),
                ]
            ),
        ]
    )
    return


if __name__ == "__main__":
    app.run()
