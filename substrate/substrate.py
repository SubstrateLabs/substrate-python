import json
from typing import Optional, Any, Dict

import zlib
import base64

from substrate.streaming import SubstrateStreamingResponse

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
        timeout: float = 60 * 5.0,
        additional_headers: Optional[Dict[str, Any]] = None,
    ):
        """
        Initialize the Substrate SDK.
        """
        if additional_headers is None:
            additional_headers = {}
        self.api_key = api_key
        self._client = APIClient(
            api_key=api_key,
            base_url=base_url,
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

    def stream(self, *nodes: CoreNode) -> SubstrateStreamingResponse:
        """
        Run the given nodes and receive results as Server-Sent Events.
        """
        serialized = Substrate.serialize(*nodes)
        iterator = self._client.post_compose_streaming(dag=serialized)
        return SubstrateStreamingResponse(iterator=iterator)

    async def async_stream(self, *nodes: CoreNode) -> SubstrateStreamingResponse:
        """
        Run the given nodes and receive results as Server-Sent Events.
        """
        serialized = Substrate.serialize(*nodes)
        iterator = await self._client.async_post_compose_streaming(dag=serialized)
        return SubstrateStreamingResponse(iterator=iterator)

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

        all_nodes = set()

        def collect_nodes(node):
            all_nodes.add(node)
            for referenced_node in node.referenced_nodes:
                collect_nodes(referenced_node)

        for node in nodes:
            collect_nodes(node)

        graph = Graph()
        for node in all_nodes:
            if not graph.DAG.has_node(node):
                graph.add_node(node)
            for depend_node in node.explicit_depends:
                graph.add_edge(depend_node, node)
        graph_serialized = graph.to_dict()
        return graph_serialized
