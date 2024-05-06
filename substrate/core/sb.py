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
    ShortCircuitDirective,
    ShortCircuitInputTarget,
    ShortCircuitConditionTarget,
)

StringConcatable = Union[str, None, Future]
JQCompatible = Union[Future, JQTargetType]
ConditionCompatible = Union[Future, bool]


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

    @classmethod
    def when(cls, condition: ConditionCompatible, input: Union[Future, Any]) -> Any:
        """
        Short-circuiting conditional edge.
        Only evaluate the subsequent node with the provided input if the condition is true.
        :param condition: A boolean or a future reference to a boolean.
        :param input: A future reference to the output of another node.
        :return: A future reference to the short-circuiting `when` operator.
        """
        c_future_id = condition.id if isinstance(condition, Future) else None
        c_val = condition if not isinstance(condition, Future) else None
        i_future_id = input.id if isinstance(input, Future) else None
        i_val = input if not isinstance(input, Future) else None
        directive = ShortCircuitDirective(
            condition=ShortCircuitConditionTarget(future_id=c_future_id, val=c_val),
            input=ShortCircuitInputTarget(future_id=i_future_id, val=i_val),
        )
        result = Future(directive=directive)
        # add edge to the condition future
        if isinstance(condition, Future):
            result.FutureG.add_edge(condition, result)
        # add edge to the input future
        if isinstance(input, Future):
            result.FutureG.add_edge(input, result)
        return result  # type: ignore
