import os
import sys
from pathlib import Path

# add parent dir to sys.path to make 'substrate' importable
parent_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(parent_dir))

api_key = os.environ.get("SUBSTRATE_API_KEY")
if api_key is None:
    raise EnvironmentError("No SUBSTRATE_API_KEY set")

from substrate import Substrate, GenerateText, sb

a = GenerateText({"prompt": "Give me a random number. Return only the number, with no additional text."}).subscribe()
b = GenerateText(
    {
        "prompt": sb.concat("multiply NUMBER by 8. NUMBER: ", a.future.text, "\n Return only the number, no text"),
        # "foo": "bar",
    }
).subscribe()

s = Substrate(api_key=api_key)
res = s.run(a, b)
a_out = a.output(res)


print(a_out.text)
