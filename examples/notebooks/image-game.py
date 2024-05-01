import marimo

__generated_with = "0.3.12"
app = marimo.App(width="medium")


@app.cell
def __():
    # enter your API key (or store it in the SUBSTRATE_API_KEY env var)
    import os

    api_key = os.environ.get("SUBSTRATE_API_KEY")
    api_key = api_key or "YOUR_API_KEY"
    return api_key, os


@app.cell(hide_code=True)
def __(api_key):
    # import modules + initialize substrate
    import time
    import datetime
    import json
    import string
    import random
    import base64
    import marimo as mo
    import substrate as sb

    substrate = sb.Substrate(
        api_key=api_key,
        backend="v1",
    )
    return base64, datetime, json, mo, random, sb, string, substrate, time


@app.cell
def __(datetime, mo, sb, substrate):
    # create a vector store
    now = datetime.datetime.now()
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    start_of_day_ts = int(start_of_day.timestamp())
    collection_name = f"image_test_{start_of_day_ts}"
    mo.md(f"collection name: {collection_name}")
    create_vstore = sb.CreateVectorStore(
        {"model": "clip", "collection_name": collection_name}
    )
    create_res = substrate.run(create_vstore)
    mo.accordion({"response": mo.tree(create_res.json)})
    return (
        collection_name,
        create_res,
        create_vstore,
        now,
        start_of_day,
        start_of_day_ts,
    )


@app.cell(hide_code=True)
def __(mo):
    prompt = mo.ui.text(
        placeholder="prompt",
        label="Enter a secret image prompt",
        value="A bowl of fruit",
        kind="password",
        full_width=True,
    ).form()
    prompt
    return prompt,


@app.cell
def __(collection_name, mo, prompt, sb, substrate):
    # generate an image and embed it
    image = sb.GenerateImage(
        {
            "prompt": prompt.value,
        }
    )
    embed = sb.EmbedImage(
        {
            "image_uri": image.future.image_uri,
            "collection_name": collection_name,
        }
    )
    res = substrate.run(image, embed)
    mo.accordion({"response": mo.tree(res.json)})
    return embed, image, res


@app.cell(hide_code=True)
def __(embed, image, mo, res):
    mo.vstack(
        [
            mo.image(src=res.get(image).image_uri, width=400),
            mo.md(f"embedding id: `{res.get(embed).embedding.doc_id}`"),
        ]
    )
    return


@app.cell
def __(mo):
    guesses = (
        mo.md(
            """
        ### Let two other people try to generate a similar image:
        - Guess prompt 1 {guess1}
        - Guess prompt 2 {guess2}
        """
        )
        .batch(
            guess1=mo.ui.text(full_width=True), guess2=mo.ui.text(full_width=True)
        )
        .form()
    )
    guesses
    return guesses,


@app.cell
def __(collection_name, guesses, sb):
    # Generate and embed the images
    guess1image = sb.GenerateImage(
        {
            "prompt": guesses.value["guess1"],
        }
    )
    guess2image = sb.GenerateImage(
        {
            "prompt": guesses.value["guess2"],
        }
    )
    embed1 = sb.EmbedImage(
        {
            "image_uri": guess1image.future.image_uri,
            "collection_name": collection_name,
        }
    )
    embed2 = sb.EmbedImage(
        {
            "image_uri": guess2image.future.image_uri,
            "collection_name": collection_name,
        }
    )
    return embed1, embed2, guess1image, guess2image


@app.cell
def __(embed1, embed2, guess1image, guess2image, mo, substrate):
    guess_res = substrate.run(guess1image, guess2image, embed1, embed2)
    mo.accordion({"response": mo.tree(guess_res.json)})
    return guess_res,


@app.cell
def __(embed1, embed2, guess_res, mo):
    image1_embed_id = guess_res.get(embed1).embedding.doc_id
    image2_embed_id = guess_res.get(embed2).embedding.doc_id
    mo.accordion(
        {"ids": mo.tree({"image1": image1_embed_id, "image2": image2_embed_id})}
    )
    return image1_embed_id, image2_embed_id


@app.cell
def __(collection_name, guess1image, guess2image, guess_res, sb):
    # query with the embeddings of the two image guesses
    query = sb.QueryVectorStore(
        {
            "model": "clip",
            "collection_name": collection_name,
            "query_image_uris": [
                guess_res.get(guess1image).image_uri,
                guess_res.get(guess2image).image_uri,
            ],
            "top_k": 100,
            "ef_search": 64,
        }
    )
    return query,


@app.cell
def __(mo, query, substrate):
    query_res = substrate.run(query)
    query_items = query_res.get(query).results
    mo.accordion({"items": mo.tree(query_items)})
    return query_items, query_res


@app.cell
def __(embed, mo, query_items, res):
    # get the similarity of the two guesses to the original image
    orig_embed_id = res.get(embed).embedding.doc_id
    match1 = next((i for i in query_items[0] if i.id == orig_embed_id), None)
    match2 = next((i for i in query_items[1] if i.id == orig_embed_id), None)
    match1_wins = match1.distance < match2.distance

    mo.accordion(
        {
            "result": mo.tree(
                {
                    "orig_embed_id": orig_embed_id,
                    "image1_distance": match1.distance,
                    "image2_distance": match2.distance,
                    "match1_wins": match1_wins,
                }
            )
        }
    )
    return match1, match1_wins, match2, orig_embed_id


@app.cell
def __(
    guess1image,
    guess2image,
    guess_res,
    guesses,
    image,
    match1,
    match1_wins,
    match2,
    mo,
    prompt,
    res,
):
    mo.hstack(
        [
            mo.vstack(
                [
                    mo.image(src=res.get(image).image_uri),
                    mo.md(f"Original prompt: {prompt.value}"),
                ]
            ),
            mo.vstack(
                [
                    mo.image(src=guess_res.get(guess1image).image_uri),
                    mo.md(f"Guess 1: {guesses.value["guess1"]}"),
                    mo.md(f"Distance: {match1.distance}"),
                    mo.md(f"**{'WINNER' if match1_wins else 'LOSER'}**"),
                ]
            ),
            mo.vstack(
                [
                    mo.image(src=guess_res.get(guess2image).image_uri),
                    mo.md(f"Guess 2: {guesses.value["guess2"]}"),
                    mo.md(f"Distance: {match2.distance}"),
                    mo.md(f"**{'LOSER' if match1_wins else 'WINNER'}**"),
                ]
            ),
        ]
    )
    return


if __name__ == "__main__":
    app.run()
