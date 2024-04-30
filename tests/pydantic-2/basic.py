import os

api_key = os.environ.get("SUBSTRATE_API_KEY")
if api_key is None:
    raise EnvironmentError("No SUBSTRATE_API_KEY set")

from substrate import Substrate, GenerateText

substrate = Substrate(api_key=api_key)

story = GenerateText({"prompt": "tell me a story", "max_tokens": 8})
response = substrate.run(story)

summary_out = response.get(story)
print(summary_out.text)
