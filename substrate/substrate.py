import json
import zlib
import base64
from typing import Any, Dict

from ._client import APIClient
from .core.corenode import CoreNode
from .core.client.graph import Graph
from .substrate_response import SubstrateResponse


class Substrate:
    """
    Substrate client.
    """

    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.substrate.run",
        backend: str = "v1",
        timeout: float = 60 * 5.0,
        additional_headers: Dict[str, Any] = {},
    ):
        """
        Initialize the Substrate SDK.
        """
        self.api_key = api_key
        self._client = APIClient(
            api_key=api_key,
            base_url=base_url,
            backend=backend,
            timeout=timeout,
            additional_headers=additional_headers,
        )

    def run(self, *nodes: CoreNode) -> SubstrateResponse:
        """
        Run the given nodes.
        """
        serialized = Substrate.serialize(*nodes)
        api_response = self._client.post_compose(dag=serialized)
        return SubstrateResponse(api_response=api_response)

    async def async_run(self, *nodes: CoreNode) -> SubstrateResponse:
        """
        Asynchronously run the given nodes.
        """
        serialized = Substrate.serialize(*nodes)
        api_response = await self._client.async_post_compose(dag=serialized)
        return SubstrateResponse(api_response=api_response)

    @staticmethod
    def visualize(*nodes):
        """
        Returns a url to visualize the given nodes.
        """
        serialized = Substrate.serialize(*nodes)
        compressed = zlib.compress(json.dumps(serialized).encode("utf-8"), level=9)
        base64_encoded = base64.b64encode(compressed).decode("utf-8")
        url_encoded = base64_encoded.replace("+", "-").replace("/", "_").replace("=", "")
        base_url = "https://explore.substrate.run/s/"
        return base_url + url_encoded

    @staticmethod
    def serialize(*nodes):
        """
        Serializes the given nodes.
        """
        graph = Graph()
        for node in nodes:
            graph.add_node(node)
        graph_serialized = graph.to_dict()
        return graph_serialized
