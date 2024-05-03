"""
CORE ꩜ SUBSTRATE
"""
from abc import ABC
from typing import (
    Dict,
    List,
    Union,
    Literal,
    Optional,
)
from dataclasses import asdict, dataclass

OpType = Literal["trace", "string-concat", "jq", "short-circuit"]


class BaseDirective(ABC):
    type: OpType

    def to_dict(self) -> Dict:
        # noinspection PyDataclass
        return asdict(self)


@dataclass
class ConcatDirectiveItem:
    future_id: Optional[str]
    val: Optional[str]


@dataclass
class ConcatDirective(BaseDirective):
    items: List[ConcatDirectiveItem]
    type: Literal["string-concat"] = "string-concat"


JQTargetType = Union[dict, list, str, int, float]


@dataclass
class JQDirectiveTarget:
    future_id: Optional[str]
    val: Optional[JQTargetType]


@dataclass
class JQDirective(BaseDirective):
    target: JQDirectiveTarget
    query: str
    type: Literal["jq"] = "jq"


@dataclass
class ShortCircuitConditionTarget:
    future_id: Optional[str]
    val: Optional[bool]


@dataclass
class ShortCircuitInputTarget:
    future_id: Optional[str]
    val: Optional[bool]


@dataclass
class ShortCircuitDirective(BaseDirective):
    condition: ShortCircuitConditionTarget
    input: ShortCircuitInputTarget
    type: Literal["short-circuit"] = "short-circuit"


TraceType = Literal["attr", "item"]


@dataclass
class TraceOperation:
    future_id: Optional[str]
    key: Optional[Union[str, int]]
    accessor: TraceType


@dataclass
class TraceDirective(BaseDirective):
    op_stack: List[TraceOperation]
    origin_node_id: Optional[str]
    type: Literal["trace"] = "trace"
