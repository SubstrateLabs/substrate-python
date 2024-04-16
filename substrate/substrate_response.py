from typing import Any, Dict, Optional

from ._client import APIResponse


class SubstrateResponse:
    """
    Substrate run response.
    """

    def __init__(self, api_response: APIResponse):
        self._api_response = api_response

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
