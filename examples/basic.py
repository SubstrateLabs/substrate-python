import os
import sys
from pathlib import Path

# add parent dir to sys.path to make 'substrate' importable
parent_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(parent_dir))

api_key = os.environ.get("SUBSTRATE_API_KEY")
if api_key is None:
    raise EnvironmentError("No SUBSTRATE_API_KEY set")

from substrate import Substrate, GenerateText

substrate = Substrate(api_key=api_key, timeout=60 * 5)

story = GenerateText(prompt="tell me a story")
# summary = GenerateText(prompt=sb.concat("Summarize this story: ", story.future.text))

# response = substrate.run(story, summary)
response = substrate.run(story)
print(response)

summary_out = response.get(story)
print(summary_out.text)

# viz = Substrate.visualize(ry)
# print(viz)
