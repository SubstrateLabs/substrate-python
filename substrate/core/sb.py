"""
CORE ꩜ SUBSTRATE
"""
from typing import Any, Union

from .client.future import Future
from .future_directive import (
    JQDirective,
    JQTargetType,
    ConcatDirective,
    JQDirectiveTarget,
    ConcatDirectiveItem,
)

StringConcatable = Union[str, None, Future]
JQCompatible = Union[Future, JQTargetType]


class sb:
    """
    Utilities for working with future references.
    """

    @classmethod
    def concat(cls, *args: StringConcatable) -> str:  # type: ignore
        """
        Concatenates strings and future references into a future reference.
        """
        if len(args) == 0:
            return ""
        elif len(args) == 1:
            return args[0]  # type: ignore
        else:
            concat_args = []
            futures = []
            for arg in args:
                is_future = isinstance(arg, Future)
                if is_future:
                    futures.append(arg)
                future_id = arg.id if is_future else None
                # if arg is None and not a future, use ""
                val = arg or "" if not is_future else None
                concat_args.append(ConcatDirectiveItem(future_id=future_id, val=val))

            directive = ConcatDirective(items=concat_args)
            result = Future(directive=directive)
            # draw edges from the concat op to all of its child futures
            for f in futures:
                result.FutureG.add_edge(f, result)
            return result  # type: ignore

    @classmethod
    def jq(cls, target: JQCompatible, query: str) -> Any:
        """
        Given a target and a query, returns a future reference to the result of the jq query.
        :param target: any future-compatible object, this can be another future, or a real value
        :param query: jq query string, e.g. ".foo.bar"
        :return: a future reference to the result of the jq query applied to the target
        """
        future_id = target.id if isinstance(target, Future) else None
        val = target if not isinstance(target, Future) else None
        directive = JQDirective(target=JQDirectiveTarget(future_id=future_id, val=val), query=query)
        result = Future(directive=directive)
        if isinstance(target, Future):
            result.FutureG.add_edge(target, result)
        return result  # type: ignore
