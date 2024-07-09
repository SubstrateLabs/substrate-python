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

from substrate import RunPython, Substrate

substrate = Substrate(api_key=api_key, timeout=60 * 5)

def print_time():
    import time
    return time.time()

a = RunPython(function=print_time)
a.id = "a"

b = RunPython(function=print_time, _depends=[a])
b.id = "b"

c = RunPython(function=print_time, _depends=[a, b])
c.id = "c"

res = substrate.run(a, b, c)
print(res.json)
