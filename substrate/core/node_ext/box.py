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
    """https://guides.substrate.run/reference/box"""

    def __init__(self, value: Union[Future, Any], hide=False, **kwargs):
        """
        Args:
            value: Value to return.

        https://guides.substrate.run/reference/box
        """
        super().__init__(value=value, hide=hide, out_type=BoxOut, **kwargs)
        self.node = "Box"
