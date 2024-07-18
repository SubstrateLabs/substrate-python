"""
CORE ꩜ SUBSTRATE
"""
import uuid
from abc import abstractmethod
from typing import Dict, List

import networkx as nx

from .corenode import CoreNode
from .base_future import BaseFuture


class CoreGraph:
    def __init__(self, id=None, initial_args=None):
        self.DAG = nx.DiGraph()
        self.initial_args = initial_args or {}
        self.id = id or f"graph_{uuid.uuid4().hex}"

    @property
    @abstractmethod
    def futures(self) -> List[BaseFuture]:
        raise NotImplementedError

    def add_edge(self, u_node: CoreNode, v_node: CoreNode, **kwargs) -> "CoreGraph":
        self.DAG.add_edge(u_node, v_node, **kwargs)
        return self

    def add_node(self, node: CoreNode) -> "CoreGraph":
        if self.DAG.has_node(node):
            raise ValueError(f"Node with id {node.id} already exists")
        self.DAG = nx.compose(self.DAG, node.SG)
        return self

    def add_nodes(self, *nodes: CoreNode) -> "CoreGraph":
        for node in nodes:
            self.add_node(node)
        return self

    def validate(self):
        if not nx.is_directed_acyclic_graph(self.DAG):
            raise ValueError("Graph should be a DAG but isn't")

    @abstractmethod
    def to_dict(self) -> Dict:
        raise NotImplementedError()
