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

a = GenerateText({"prompt": "tell me a short story in a few sentences"})
# b = GenerateText({"prompt": a.future.text})
# b = EmbedText({"text": a.future.text})

s = Substrate(api_key=api_key)
res = s.run(a, use_requests=True)


a_out = res.get(a, a.out_type)
print(a_out.text)

# b_out = res.get(b, b.out_type)
# print(type(b_out.embedding))
# print(b_out.embedding.vector)

# print("response", res.api_response.status_code)
# print("json", json.dumps(res.json, indent=2))


# a_out = a.output(res)


# print(a_out.text)
