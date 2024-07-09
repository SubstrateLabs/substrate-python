import os
import sys
from pathlib import Path
import requests
import json


response = requests.get("https://www.substrate.run/openapi.json")
openapi_spec = response.json()
openapi_version = openapi_spec["openapi"]
api_components = openapi_spec["components"]["schemas"]
api_nodes = openapi_spec["paths"]
cleaned_nodes = {key.replace("/", ""): value for key, value in api_nodes.items()}

# add parent dir to sys.path to make 'substrate' importable
parent_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(parent_dir))

api_key = os.environ.get("SUBSTRATE_API_KEY")
if api_key is None:
    raise EnvironmentError("No SUBSTRATE_API_KEY set")

from substrate import Substrate, MultiEmbedText, FindOrCreateVectorStore, DeleteVectorStore

substrate = Substrate(api_key=api_key, timeout=60 * 5, base_url="https://kube-dev.substrate.run/ray/stable")

old_collection = DeleteVectorStore(
    collection_name= "substrate_api_v2",
    model= "jina-v2"
)

collection = FindOrCreateVectorStore(
        collection_name= old_collection.future.collection_name,
        model= old_collection.future.model,
)

components_embeddings = MultiEmbedText(
        collection_name=collection.future.collection_name,
        items= [{
            "doc_id": name,
            "text": json.dumps(component),
            "metadata": {
                "type": "component"
            }
        } for name, component in api_components.items()],
)

nodes_embeddings = MultiEmbedText(
        collection_name= collection.future.collection_name,
        items= [
            {
                "doc_id": node_name,
                "text": json.dumps(node),
                "metadata": {
                    "type": "node"
                }
            } for node_name, node in cleaned_nodes.items()
        ]
)

res = substrate.run(collection, components_embeddings, nodes_embeddings)
