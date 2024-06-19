import os
import sys
import json
from pathlib import Path

# add parent dir to sys.path to make 'substrate' importable
parent_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(parent_dir))

api_key = os.environ.get("SUBSTRATE_API_KEY")
if api_key is None:
    raise EnvironmentError("No SUBSTRATE_API_KEY set")

from substrate import Substrate, ComputeText, GenerateImage, sb

substrate = Substrate(api_key=api_key, timeout=60 * 5)

scene = ComputeText(prompt="description of a mythical forest creature: ")

styles = ["woodblock printed", "art nouveau poster"]
images = [GenerateImage(store="hosted", prompt=sb.concat(style, ": ", scene.future.text)) for style in styles]

result = substrate.run(*images)

print(json.dumps(result.json, indent=2))

viz = Substrate.visualize(*images)
os.system(f"open {viz}")
