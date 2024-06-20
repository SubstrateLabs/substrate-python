import os
import sys
from pathlib import Path

from substrate.nodes import Llama3Instruct8B

# add parent dir to sys.path to make 'substrate' importable
parent_dir = Path(__file__).resolve().parent.parent.parent.parent
sys.path.insert(0, str(parent_dir))

api_key = os.environ.get("SUBSTRATE_API_KEY")
if api_key is None:
    raise EnvironmentError("No SUBSTRATE_API_KEY set")

from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from substrate import Substrate, Llama3Instruct8B

app = FastAPI()
substrate = Substrate(api_key=api_key, timeout=60 * 5)


@app.get("/qotd")
def quote_of_the_day():
    quote = Llama3Instruct8B(prompt="What's an inspirational quote of the day?")

    response = substrate.stream(quote)

    return StreamingResponse(response.iter_events(), media_type="text/event-stream")
