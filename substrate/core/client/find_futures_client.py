"""
CORE ꩜ SUBSTRATE
"""
from typing import Any, Dict, List, Union

from ..client.future import Future, TracedFuture


def find_futures_client(args: Union[Future, List[Future], Dict[str, Future], Any]) -> List[Future]:
    """
    A node can be supplied with a number of kwargs that relate to its input space. Some of
    those arg values are raw values like strings, ints, floats, etc. Others are Futures
    that resolve into raw values eventually. This function is used to find the Futures
    that are used as inputs to a node. To do this it walks the argument tree and collects
    all the Futures it finds.
    """
    futures = {}
    is_future = isinstance(args, Future)
    if is_future:
        futures[args.id] = args
        for n in args.FutureG.nodes():
            if n.id == args.id:
                continue
            # Traced futures can be thought of as linked lists, and we'll have
            # many instrumental futures along the way. Here we're only interested
            # in terminal TracedFutures, which have the entire op_stack.
            if isinstance(n, TracedFuture) and n.has_successor():
                continue
            sub_futures = find_futures_client(n)
            futures.update({f.id: f for f in sub_futures})
    elif isinstance(args, dict):
        for _, v in args.items():
            # TODO(rob) handle finding key futures with something like
            # futures.update({f.id: f for f in futures_from_client_args(k)})
            futures.update({f.id: f for f in find_futures_client(v)})
    elif isinstance(args, list):
        for item in args:
            sub_futures = find_futures_client(item)
            futures.update({f.id: f for f in sub_futures})

    return list(futures.values())
