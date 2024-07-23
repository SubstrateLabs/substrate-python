import os
import json

api_key = os.environ.get("SUBSTRATE_API_KEY")
if api_key is None:
    raise EnvironmentError("No SUBSTRATE_API_KEY set")

from substrate import (
    Substrate,
    EraseImage,
    InpaintImage,
    GenerateImage,
    RemoveBackground,
)

substrate = Substrate(api_key=api_key, timeout=60 * 5)
prompt = "by edward hopper, a red leather wing chair in an open room, pillars, amazing painting composition"
image = GenerateImage(prompt=prompt)
mask = RemoveBackground(
    image_uri=image.future.image_uri,
    return_mask=True,
)
bg = EraseImage(
    image_uri=image.future.image_uri,
    mask_image_uri=mask.future.image_uri,
)
bg_prompt = "by edward hopper, an empty room with pillars, amazing painting composition"
inpaint = InpaintImage(image_uri=bg.future.image_uri, prompt=bg_prompt, store="hosted")
result = substrate.run(inpaint)
viz = Substrate.visualize(inpaint)
os.system(f"open {viz}")

print(json.dumps(result.json, indent=2))
