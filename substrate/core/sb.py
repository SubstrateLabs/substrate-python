"""
CORE ꩜ SUBSTRATE
"""
from typing import Union

from .base_future import Concatable, ConcatDirective
from .client.future import Future

StringConcatable = Union[str, None, Future]


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
                concat_args.append(
                    Concatable(
                        future_id=arg.id if is_future else None,
                        # if arg is None and not a future, use ""
                        val=arg or "" if not is_future else None,
                    )
                )

            directive = ConcatDirective(type="string-concat", items=concat_args)
            os = Future(directive=directive)
            # draw edges from the concat op to all of its child futures
            for f in futures:
                os.FutureG.add_edge(f, os)
            return os  # type: ignore
