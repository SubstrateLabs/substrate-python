"""
CORE ꩜ SUBSTRATE
"""
import json
from typing import Dict, List

from ..coregraph import CoreGraph
from ..base_future import BaseFuture


class Graph(CoreGraph):
    """
    Client side representation of a Substrate graph.
    Not exposed to users – `substrate.run()` creates the serialized graph
    """

    def to_dict(self) -> Dict:
        as_dict = {
            "nodes": [n.to_dict() for n in self.DAG.nodes()],
            "edges": [(u.id, v.id, d) for u, v, d in list(self.DAG.edges.data())],
            "initial_args": self.initial_args,
            "futures": [future.to_dict() for future in self.futures],
            "id": self.id,
        }
        return json.loads(json.dumps(as_dict))

    @property
    def futures(self) -> List[BaseFuture]:
        """
        Go through the futures from the node arg entrypoints and return a list of all futures linked to those futures
        This is a derived property because the future list is dynamic based on program state. Once we invoke this
        to e.g. render a graph into json, it becomes static.
        """
        futures = {f.id: f for node in self.DAG.nodes() for f in node.dependent_futures}
        return list(futures.values())
