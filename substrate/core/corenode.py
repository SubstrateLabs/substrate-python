"""
CORE ꩜ SUBSTRATE
"""
from typing import Any, List, Type

import networkx as nx

from .base_future import BaseFuture
from .id_generator import IDGenerator
from .client.future import TracedFuture
from .future_directive import TraceDirective
from .client.find_futures_client import find_futures_client


class CoreNode:
    def __init__(self, hide: bool = False, **attr):
        self.node = self.__class__.__name__
        self.args = attr
        generator_instance = IDGenerator.get_instance(self.__class__.__name__)
        self.id = generator_instance.get_next_id()
        self._global_output_keys = None
        self._should_output_globally: bool = not hide
        self.SG = nx.DiGraph()
        if attr:
            self.args = BaseFuture.replace_futures_with_placeholder(attr)
        else:
            self.args = {}
        self.SG.add_node(self, **self.args)
        self.futures_from_args: List[BaseFuture] = find_futures_client(attr)

    @property
    def out_type(self) -> Type[Any]:
        """
        Get the typed output of this node using `response.get(node, node.out_type)`
        """
        return Type[None]

    def to_dict(self):
        return {
            "id": self.id,
            "node": self.node,
            "args": self.args,
            **({"_should_output_globally": self._should_output_globally} if self._should_output_globally else {}),
            **({"_global_output_keys": self._global_output_keys} if self._global_output_keys else {}),
        }

    @property
    def future(self) -> TracedFuture:
        """
        Reference to future output of this node.
        """
        return TracedFuture(directive=TraceDirective(op_stack=[], origin_node_id=self.id))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id})"

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return isinstance(other, CoreNode) and self.id == other.id
