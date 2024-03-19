from ._client import APIClient, APIResponse
from .core.corenode import CoreNode
from .core.client.graph import Graph


class SubstrateResponse:
    """
    Substrate run response.
    """

    def __init__(self, api_response: APIResponse):
        self._api_response = api_response

    @property
    def api_response(self) -> APIResponse:
        """
        The raw API response.
        """
        return self._api_response


class SubstrateBase:
    def __init__(self, api_key: str):
        """
        Initialize the Substrate SDK.
        """
        self.api_key = api_key
        self._client = APIClient(api_key=api_key, base_url="https://api.substrate.run")


class Substrate(SubstrateBase):
    """
    Substrate client.
    """

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


class AsyncSubstrate(SubstrateBase):
    """
    Async Substrate client.
    """

    async def run(self, *nodes: CoreNode) -> SubstrateResponse:
        """
        Run the given nodes.
        """
        graph = Graph()
        for node in nodes:
            graph.add_node(node)
        graph_serialized = graph.to_dict()
        api_response = await self._client.async_post_compose(dag=graph_serialized)
        return SubstrateResponse(api_response=api_response)
