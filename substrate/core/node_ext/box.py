from typing import Any, Union

from pydantic import Extra, BaseModel

from ..corenode import CoreNode
from ..client.future import Future


class BoxIn(BaseModel):
    class Config:
        extra = Extra.allow

    value: Any


class BoxOut(BaseModel):
    class Config:
        extra = Extra.allow

    value: Any
    """
    Resulting value.
    """


class Box(CoreNode[BoxOut]):
    """https://substrate.run/nodes#Box"""

    def __init__(self, value: Union[Future, Any], **kwargs):
        """
        Args:
            value: Value to return.

        https://substrate.run/nodes#Box
        """
        super().__init__(value=value, **kwargs)
        self.node = "Box"
