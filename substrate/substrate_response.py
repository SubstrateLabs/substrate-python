from typing import Any, Dict, TypeVar, Optional

from ._client import APIResponse
from .core.corenode import CoreNode

OT = TypeVar("OT", bound=Any)


class SubstrateResponse:
    """
    Substrate run response.
    """

    def __init__(self, api_response: APIResponse):
        self._api_response = api_response

    def get(self, node: CoreNode[OT]) -> OT:
        """
        Get the output of a specific node.
        """
        if self.json and self.json.get("data"):
            data = self.json["data"]
            if data.get(node.id):
                node_json = data[node.id]
                return node.out_type(**node_json)
        raise ValueError(f"Node {node.id} not found in response")

    @property
    def json(self) -> Optional[Dict[str, Any]]:
        """
        The full JSON response.
        """
        return self._api_response.json

    @property
    def api_response(self) -> APIResponse:
        """
        The raw API response object.
        """
        return self._api_response
