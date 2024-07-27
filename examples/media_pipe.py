import os
import json

from substrate import Substrate, Firellava13B, GenerateImage, sb

api_key = os.environ.get("SUBSTRATE_API_KEY")
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
