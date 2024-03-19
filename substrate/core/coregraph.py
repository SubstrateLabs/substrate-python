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
    def __init__(self, id=None, **initial_args):
        self.DAG = nx.DiGraph()
        self.initial_args = initial_args
        self.id = id or f"graph_{uuid.uuid4().hex}"

    def has_futures(self) -> bool:
        for n in self.DAG.nodes():
            if n.futures_from_args:
                return True
        return False

    @property
    @abstractmethod
    def futures(self) -> List[BaseFuture]:
        raise NotImplementedError

    def add_node(self, node: CoreNode) -> "CoreGraph":
        self.DAG = nx.compose(self.DAG, node.SG)
        return self

    def add_nodes(self, *nodes: CoreNode) -> "CoreGraph":
        for node in nodes:
            self.add_node(node)
        return self

    def _check_dag(self):
        if not nx.is_directed_acyclic_graph(self.DAG):
            raise ValueError("Graph should be a DAG but isn't")

    @abstractmethod
    def to_dict(self) -> Dict:
        raise NotImplementedError()
