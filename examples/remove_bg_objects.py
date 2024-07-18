import os
import json

api_key = os.environ.get("SUBSTRATE_API_KEY")
if api_key is None:
    raise EnvironmentError("No SUBSTRATE_API_KEY set")

from substrate import (
    Substrate,
    GenerateImage,
    RemoveBackground,
    EraseImage,
    InpaintImage,
    ComputeJSON,
    sb,
    ComputeText,
    Box,
)

substrate = Substrate(api_key=api_key, timeout=60 * 5)
num_images = 2
object_name = "a red leather wing chair"
artists = [
    ComputeText(
        prompt="respond with just the name of a 20th century painter (moma, whitney): ", max_tokens=10, temperature=1
    )
    for _ in range(num_images)
]
prompt_for = lambda x: sb.concat("by ", x, object_name, " in an open room, pillars, amazing painting composition")
bg_prompt_for = lambda x: sb.concat("by ", x, "an empty room with pillars, amazing painting composition")
images = [GenerateImage(prompt=prompt_for(artist.future.text), _cache_age=1000) for artist in artists]
removals = [RemoveBackground(image_uri=image.future.image_uri) for image in images]
masks = [RemoveBackground(image_uri=image.future.image_uri, return_mask=True) for image in images]
bg_images = [
    EraseImage(image_uri=image.future.image_uri, mask_image_uri=mask.future.image_uri)
    for image, mask in zip(images, masks)
]
inpainted_images = [
    InpaintImage(image_uri=bg_image.future.image_uri, prompt=bg_prompt_for(artist.future.text), store="hosted")
    for bg_image, artist in zip(bg_images, artists)
]
final = Box(value=[inpainted_image.future.image_uri for inpainted_image in inpainted_images])
result = substrate.run(final)
viz = Substrate.visualize(final)
os.system(f"open {viz}")

print(json.dumps(result.json, indent=2))
