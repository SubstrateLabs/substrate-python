"""
CORE ꩜ SUBSTRATE
"""
from typing import Any, Dict, Generic, TypeVar, Optional

from .id_generator import IDGenerator
from .future_directive import BaseDirective

FUTURE_ID_PLACEHOLDER = "__$$SB_GRAPH_OP_ID$$__"

T = TypeVar("T", bound=BaseDirective)


class BaseFuture(Generic[T]):
    def __init__(self, directive: T, id: Optional[str] = None):
        generator_instance = IDGenerator.get_instance("future")
        self.id: str = id or generator_instance.get_next_id()
        self.directive = directive

    def to_placeholder(self):
        return {FUTURE_ID_PLACEHOLDER: self.id}

    def to_dict(self) -> Dict:
        return {"id": self.id, "directive": self.directive.to_dict()}

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id})"

    @classmethod
    def replace_futures_with_placeholder(cls, args: Dict[str, Any]):
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
