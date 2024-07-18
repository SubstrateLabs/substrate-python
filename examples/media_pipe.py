import os
import json

api_key = os.environ.get("SUBSTRATE_API_KEY")
if api_key is None:
    raise EnvironmentError("No SUBSTRATE_API_KEY set")

from substrate import Substrate, ComputeText, GenerateImage, sb, ComputeJSON, Firellava13B

substrate = Substrate(api_key=api_key, timeout=60 * 5)
schema = {
    "type": "object",
    "properties": {
        "main_object": {"type": "string"},
        "replacement": {"type": "string"},
    },
    "required": ["main_object"],
}
image_uri = "https://media.substrate.run/desk.jpeg"

replacement = Firellava13B(
    prompt="Identify the main object in the image. Then think of something funny to replace it with. Respond with the replacement. Your answer should be only one or two words.",
    image_uris=[image_uri],
)
image = GenerateImage(prompt=sb.concat("a picture of a ", replacement.future.text), image_uri=image_uri, store="hosted")
result = substrate.run(image)
viz = Substrate.visualize(image)
os.system(f"open {viz}")

print(json.dumps(result.json, indent=2))
# fg = RemoveBackground(image_uri=image.future.image_uri)
# mask = RemoveBackground(
#     image_uri=image.future.image_uri,
#     return_mask=True,
# )
# bg = EraseImage(
#     image_uri=image.future.image_uri,
#     mask_image_uri=mask.future.image_uri,
# )
# bg_prompt = "empty dark majestic room, celestial galaxy wallpaper, high resolution AD"
# inpaint = InpaintImage(image_uri=bg.future.image_uri, prompt=bg_prompt)
#
# scene = ComputeText(prompt="description of a mythical forest creature: ")
#
# styles = ["woodblock printed", "art nouveau poster"]
# images = [GenerateImage(store="hosted", prompt=sb.concat(style, ": ", scene.future.text)) for style in styles]
#
# result = substrate.run(*images)
#
# print(json.dumps(result.json, indent=2))
#
# viz = Substrate.visualize(*images)
# os.system(f"open {viz}")
