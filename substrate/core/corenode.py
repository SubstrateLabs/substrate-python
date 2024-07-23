"""
CORE ꩜ SUBSTRATE

NOTE: this file is not copied from the main repo
"""
from typing import Any, List, Type, Generic, TypeVar, Optional

import networkx as nx

from .base_future import BaseFuture
from .id_generator import IDGenerator
from .client.future import Future, TracedFuture
from .future_directive import TraceDirective
from .client.find_futures_client import find_futures_client

OT = TypeVar("OT")


class CoreNode(Generic[OT]):
    def __init__(
        self,
        out_type: Type[OT] = Type[Any],
        hide: bool = True,
        _cache_age: Optional[int] = None,
        _cache_keys: Optional[List[str]] = None,
        _max_retries: Optional[int] = None,
        _depends: Optional[List["CoreNode"]] = None,
        **attr,
    ):
        self._out_type = out_type
        self.node = self.__class__.__name__
        self.init_attrs = attr
        generator_instance = IDGenerator.get_instance(self.__class__.__name__)
        self.id = generator_instance.get_next_id()
        self._cache_age = _cache_age
        self._cache_keys = _cache_keys
        self._max_retries = _max_retries
        self._depends = [] if _depends is None else _depends
        self._should_output_globally: bool = not hide
        self.SG = nx.DiGraph()
        if attr:
            self.args = BaseFuture.replace_futures_with_placeholder(attr)
        else:
            self.args = {}
        self.SG.add_node(self, **self.args)
        self.futures_from_args: List[Future] = find_futures_client(attr)
        self.referenced_nodes = [
            future.directive.origin_node for future in self.futures_from_args if isinstance(future, TracedFuture)
        ]

        for depend_node in self._depends:
            for referenced_node in depend_node.referenced_nodes:
                self.referenced_nodes.append(referenced_node)
            for referenced_future in depend_node.futures_from_args:
                self.futures_from_args.append(referenced_future)

    @property
    def explicit_depends(self) -> List["CoreNode"]:
        return self._depends

    @property
    def dependent_futures(self) -> List[Future]:
        return find_futures_client(self.init_attrs)

    @property
    def out_type(self) -> Type[OT]:
        """
        The output type of this node.
        """
        return self._out_type

    def to_dict(self):
        return {
            "id": self.id,
            "node": self.node,
            "args": self.args,
            **({"_should_output_globally": self._should_output_globally} if self._should_output_globally else {}),
            **({"_cache_age": self._cache_age} if self._cache_age else {}),
            **({"_cache_keys": self._cache_keys} if self._cache_keys else {}),
            **({"_max_retries": self._max_retries} if self._max_retries else {}),
        }

    def subscribe(self):
        self._should_output_globally = True
        return self

    @property
    def future(self) -> TracedFuture:
        """
        Reference to future output of this node.
        """
        return TracedFuture(directive=TraceDirective(op_stack=[], origin_node=self))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id})"

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return isinstance(other, CoreNode) and self.id == other.id
