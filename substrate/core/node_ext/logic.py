from typing import Any, Union, Optional

from pydantic import Extra, BaseModel

from ..sb import ConditionCompatible
from ..corenode import CoreNode
from ..client.future import Future


class IfIn(BaseModel):
    class Config:
        extra = Extra.allow

    condition: bool
    value_if_true: Any
    value_if_false: Optional[Any] = None


class IfOut(BaseModel):
    class Config:
        extra = Extra.allow

    result: Any
    """
    Resulting value.
    """


class If(CoreNode[IfOut]):
    """https://substrate.run/nodes#If"""

    def __init__(
        self,
        condition: ConditionCompatible,
        value_if_true: Union[Future, Any],
        value_if_false: Optional[Union[Future, Any]] = None,
        **kwargs,
    ):
        """
        Args:
            condition: Condition to check.
            value_if_true: Value to return if condition is true.
            value_if_false: Value to return if condition is false.

        https://substrate.run/nodes#If
        """
        super().__init__(
            condition=condition,
            value_if_true=value_if_true,
            value_if_false=value_if_false,
            out_type=IfOut,
            **kwargs,
        )
        self.node = "LogicalIf"
