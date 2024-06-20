import json
from typing import Iterator, AsyncIterator

import httpx_sse


class ServerSentEvent:
    def __init__(self, event: httpx_sse.ServerSentEvent):
        self.event = event

    @property
    def data(self):
        return json.loads(self.event.data)

    def __repr__(self):
        return self.event.__repr__()

    def __str__(self):
        """
        Render the Server-Sent Event as a string to be rendered in a streaming response
        """
        fields = ["id", "event", "data", "retry"]
        lines = [f"{field}: {getattr(self.event, field)}" for field in fields if getattr(self.event, field)]
        return "\n".join(lines) + "\n\n"


class SubstrateStreamingResponse:
    """
    Substrate stream response.
    """

    def __init__(self, *, iterator):
        self.iterator = iterator

    def iter(self) -> Iterator[ServerSentEvent]:
        for sse in self.iterator:
            yield ServerSentEvent(sse)

    def iter_events(self) -> Iterator[str]:
        for sse in self.iterator:
            yield str(ServerSentEvent(sse))

    async def async_iter(self) -> Iterator[ServerSentEvent]:
        async for sse in self.iterator:
            yield ServerSentEvent(sse)

    async def async_iter_events(self) -> AsyncIterator[str]:
        async for sse in self.iterator:
            yield str(ServerSentEvent(sse))
