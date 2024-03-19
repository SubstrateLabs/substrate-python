"""
CORE ꩜ SUBSTRATE
"""
from typing import (
    Any,
    Dict,
    List,
    Union,
    Literal,
    Optional,
)
from dataclasses import asdict, dataclass

from .id_generator import IDGenerator

FUTURE_ID_PLACEHOLDER = "__$$SB_GRAPH_OP_ID$$__"


OpType = Literal["trace", "string-concat"]
TraceType = Literal["attr", "item"]
ConcatDirection = Literal["left", "right"]


@dataclass
class Concatable:
    future_id: Optional[str]
    val: Optional[str]


@dataclass
class ConcatDirective:
    items: List[Concatable]
    type: Literal["string-concat"] = "string-concat"


@dataclass
class TraceOperation:
    future_id: Optional[str]
    key: Optional[Union[str, int]]
    accessor: TraceType


@dataclass
class TraceDirective:
    op_stack: List[TraceOperation]
    origin_node_id: Optional[str]
    type: Literal["trace"] = "trace"


Directive = Union[TraceDirective, ConcatDirective]


class BaseFuture:
    def __init__(
        self,
        directive: Directive,
        id: Optional[str] = None,
    ):
        generator_instance = IDGenerator.get_instance("future")
        self.id: str = id or generator_instance.get_next_id()
        self.directive: Directive = directive

    def to_placeholder(self):
        return {FUTURE_ID_PLACEHOLDER: self.id}

    def to_dict(self) -> Dict:
        return {"id": self.id, "directive": asdict(self.directive)}

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id})"

    @staticmethod
    def replace_futures_with_placeholder(args: Dict[str, Any]):
        if isinstance(args, BaseFuture):
            return args.to_placeholder()
        elif isinstance(args, dict):
            val = {}
            for k, v in args.items():
                # TODO(rob) some way to handle futures in the key space - may need to change
                # the placeholder scheme to be something else, like {"OP_ID_PLACEHOLDER(future_id)": val}
                val[k] = BaseFuture.replace_futures_with_placeholder(v)
            return val
        elif isinstance(args, list):
            return [BaseFuture.replace_futures_with_placeholder(item) for item in args]
        return args
