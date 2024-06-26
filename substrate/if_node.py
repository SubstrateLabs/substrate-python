from typing import Any, Union, Optional

from .core.sb import ConditionCompatible
from .core.models import IfOut
from .core.corenode import CoreNode
from .core.client.future import Future
from .future_dataclass_models import FutureIfOut


class If(CoreNode[IfOut]):
    """https://substrate.run/nodes#If"""

    def __init__(
        self,
        condition: ConditionCompatible,
        value_if_true: Union[Future, Any],
        value_if_false: Optional[Union[Future, Any]] = None,
        hide: bool = False,
        **kwargs,
    ):
        """
        Args:
            condition: Condition.
            value_if_true: Result when condition is true.
            value_if_false: Result when condition is false.

        https://substrate.run/nodes#If
        """
        super().__init__(
            condition=condition,
            value_if_true=value_if_true,
            value_if_false=value_if_false,
            hide=hide,
            out_type=IfOut,
            **kwargs,
        )
        self.node = "LogicalIf"

    @property
    def future(self) -> FutureIfOut:  # type: ignore
        """
        Future reference to this node's output.

        https://substrate.run/nodes#If
        """
        return super().future  # type: ignore
