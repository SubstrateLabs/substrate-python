"""
CORE ꩜ SUBSTRATE

NOTE: this file is not copied from the main repo
"""
from abc import ABC
from typing import (
    Any,
    Dict,
    List,
    Union,
    Literal,
    Optional,
)
from dataclasses import asdict, dataclass

OpType = Literal["trace", "string-concat", "jq", "jinja"]


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
class JinjaTemplate:
    future_id: Optional[str]
    val: Optional[str]


@dataclass
class JinjaDirective(BaseDirective):
    template: JinjaTemplate
    variables: Dict[str, Any]
    type: Literal["jq"] = "jinja"

    def to_dict(self) -> Dict:
        from .base_future import BaseFuture

        replaced = BaseFuture.replace_futures_with_placeholder(self.variables)
        return {
            "type": self.type,
            "template": asdict(self.template),
            "variables": replaced,
        }


TraceType = Literal["attr", "item"]


@dataclass
class TraceOperation:
    future_id: Optional[str]
    key: Optional[Union[str, int]]
    accessor: TraceType


@dataclass
class TraceDirective(BaseDirective):
    op_stack: List[TraceOperation]
    origin_node: "CoreNode"
    type: Literal["trace"] = "trace"

    def to_dict(self) -> Dict:
        # noinspection PyDataclass
        return {
            "op_stack": [asdict(item) for item in self.op_stack],
            "origin_node_id": self.origin_node.id,
            "type": self.type,
        }
