import os
import sys
from pathlib import Path
import requests
import json

from substrate.nodes import ComputeText


# add parent dir to sys.path to make 'substrate' importable
parent_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(parent_dir))

api_key = os.environ.get("SUBSTRATE_API_KEY")
if api_key is None:
    raise EnvironmentError("No SUBSTRATE_API_KEY set")

from substrate import Substrate, FindOrCreateVectorStore, QueryVectorStore, BatchComputeText, sb

substrate = Substrate(api_key=api_key, timeout=60 * 5, base_url="https://kube-dev.substrate.run/ray/stable")

prompt_text = input("Enter a prompt: ")

collection = FindOrCreateVectorStore(
        collection_name= "substrate_api_v2",
        model= "jina-v2"
)

relevant_node = QueryVectorStore(
    collection_name= collection.future.collection_name,
    model=collection.future.model,
    query_strings=[prompt_text],
    top_k=1,
    include_metadata=True,
    include_values=True,
    filters={
        "type": {"$eq": "node"}
    }
)

relevant_components = QueryVectorStore(
    collection_name= collection.future.collection_name,
    model=collection.future.model,
    top_k=5,
    query_vectors=[sb.jq(relevant_node.future.results, '.[0].[0].vector')],
    include_metadata=True,
    filters={
        "type": {"$eq": "component"}
    }
)

generated_text = ComputeText(
        prompt=sb.concat("""
You are a helpful AI assistant.  A user is going to ask you a question about
an AI platform called Substrate.  Please use the following information to summarize
the key points about Substrate.  The user is looking for a high-level overview of the
following resource:
    """,
        sb.concat(sb.jq(relevant_node.future.results, '.[0].[0].metadata.doc')),
        "The user's question is:",
        prompt_text
    )
)

res = substrate.stream(generated_text)
with open(sys.stdout.fileno(), "w") as stdout:
    for item in res.iter():
        if item.data["object"] == "node.delta":
            stdout.write(item.data.get("data", {}).get("text", ""))
