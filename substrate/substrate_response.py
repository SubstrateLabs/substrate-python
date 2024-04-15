from ._client import APIResponse


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
