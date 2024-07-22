import os

api_key = os.environ.get("SUBSTRATE_API_KEY")
from substrate import Substrate, ComputeText, sb, Box

substrate = Substrate(api_key=api_key, timeout=60 * 5, base_url="https://api-staging.substrate.run")

template = "hello {{ name }}"
box = Box(value={"rendered_string": sb.jinja(template, dict(name="world"))})
response = substrate.run(box)
print(response.json)
