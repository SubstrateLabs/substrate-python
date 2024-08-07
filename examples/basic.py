import os
import sys
from pathlib import Path

# add parent dir to sys.path to make 'substrate' importable
parent_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(parent_dir))

api_key = os.environ.get("SUBSTRATE_API_KEY")
if api_key is None:
    raise EnvironmentError("No SUBSTRATE_API_KEY set")

from substrate import Secrets, Substrate, ComputeText, sb

substrate = Substrate(
    api_key=api_key,
    secrets=Secrets(openai="YOUR_OPENAI_KEY", anthropic="YOUR_ANTHROPIC_KEY"),
)

story = ComputeText(prompt="tell me a story")
summary = ComputeText(prompt=sb.format(f"Summarize this story: {story}", story=story.future.text))

response = substrate.run(story, summary)
print(response)

print("=== story")
story_out = response.get(story)
print(story_out.text)

print("=== summary")
summary_out = response.get(summary)
print(summary_out.text)

# viz = Substrate.visualize(ry)
# print(viz)
