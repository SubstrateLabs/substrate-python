import os
import sys
import asyncio
from pathlib import Path

# add parent dir to sys.path to make 'substrate' importable
parent_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(parent_dir))

api_key = os.environ.get("SUBSTRATE_API_KEY")
if api_key is None:
    raise EnvironmentError("No SUBSTRATE_API_KEY set")

from substrate import Substrate, GenerateText, sb

substrate = Substrate(api_key=api_key, timeout=60 * 5)


a = GenerateText(prompt="tell me about windmills", max_tokens=10)
b = GenerateText(prompt=sb.concat("is this true? ", a.future.text), max_tokens=10)


async def amain():
    response = await substrate.async_stream(a, b)
    async for event in response.async_iter():
        print(event)


asyncio.run(amain())


def main():
    response = substrate.stream(a, b)
    for message in response.iter():
        print(message)


main()
