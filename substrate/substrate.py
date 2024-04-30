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
            additional_headers=additional_headers,
        )

    def run(self, *nodes: CoreNode) -> SubstrateResponse:
        """
        Run the given nodes.
        """
        graph = Graph()
        for node in nodes:
            graph.add_node(node)
        graph_serialized = graph.to_dict()
        api_response = self._client.post_compose(dag=graph_serialized)
        return SubstrateResponse(api_response=api_response)

    async def async_run(self, *nodes: CoreNode) -> SubstrateResponse:
        """
        Asynchronously run the given nodes.
        """
        graph = Graph()
        for node in nodes:
            graph.add_node(node)
        graph_serialized = graph.to_dict()
        api_response = await self._client.async_post_compose(dag=graph_serialized)
        return SubstrateResponse(api_response=api_response)
