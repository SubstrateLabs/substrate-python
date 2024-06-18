"""
CORE ꩜ SUBSTRATE

NOTE: this file is not copied from the main repo
"""
from typing import Union, TypeVar, Optional

import networkx as nx

from ..base_future import BaseFuture
from ..future_directive import TraceType, TraceDirective, TraceOperation

T = TypeVar("T", bound="BaseDirective")


class Future(BaseFuture[T]):
    def __init__(
        self,
        directive: T,
        FG: Optional["nx.DiGraph[Future]"] = None,
        **kwargs,
    ):
        super().__init__(directive, **kwargs)
        self.directive = directive
        self.FutureG = FG if FG is not None else nx.DiGraph()


class TracedFuture(Future[TraceDirective]):
    """
    You can think of this as a logical handle to a future result. This means that you can access attributes or items
    from it as if it were a resolved instance. If you use a traced future as an argument to other nodes, it will
    implicitly create an execution dependency graph. This enables you to define an inter-related graph of computations
    without worrying about the actual execution order.

    TracedFutures can create one or many future computation paths. To originate one, use Node.future. The same node
    can originate multiple separate TracedFutures, or can branch a tracing chain at any point. This makes no practical
    difference because the execution graph will end up the same.

    ```python
    a = Node(foo="bar")
    future_1 = a.future.attr1
    future_2 = a.future.attr2
    future_3 = future_1.item[0]
    future_4 = future_1.item[1].bar
    b = Node(a=future_1, b=future_2, c=future_3, d=future_4)
    ```
    """

    def __init__(
        self,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.next_id: Optional[str] = None

    def _on_access(self, key: Union[str, int, "Future"], accessor: TraceType):
        is_future = isinstance(key, Future)
        if is_future:
            self.FutureG.add_edge(key, self)
            operation = TraceOperation(future_id=key.id, accessor=accessor, key=None)
        else:
            operation = TraceOperation(key=key, accessor=accessor, future_id=None)
        next_f = TracedFuture(
            directive=TraceDirective(
                origin_node=self.directive.origin_node,
                op_stack=self.directive.op_stack + [operation],
            ),
            FG=self.FutureG,
        )
        self.next_id = next_f.id
        return next_f

    def __getattr__(self, key: Union[str, "Future"]):
        return self._on_access(key, "attr")

    def __getitem__(self, key: Union[int, "Future"]):
        return self._on_access(key, "item")

    def is_terminal(self):
        return self.next_id is None

    def has_successor(self):
        return not self.is_terminal()
