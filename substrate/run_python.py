from typing import Any, Dict, List, Callable, Optional

from .core.models import RunPythonOut
from .core.corenode import CoreNode
from .future_dataclass_models import FutureRunPythonOut


class RunPython(CoreNode[RunPythonOut]):
    """https://substrate.run/nodes#RunPython"""

    def __init__(
        self,
        function: Callable,
        kwargs: Dict[str, Any] = {},
        pip_install: Optional[List[str]] = None,
        hide: bool = False,
    ):
        """
        Args:
            function: The function to run remotely.
            kwargs: Keyword arguments to your function. This can include future references to the output of previous nodes.
            pip_install: List of pip dependencies to install in your function's sandbox

        https://guides.substrate.run/reference/run-python
        """
        import sys
        import base64

        import cloudpickle

        og_module = function.__module__
        function.__module__ = "__main__"
        fn_bytes = cloudpickle.dumps(function)
        function.__module__ = og_module
        fn_str = base64.b64encode(fn_bytes).decode("utf-8")

        python_version = sys.version.split()[0]
        super().__init__(
            pkl_function=fn_str,
            kwargs=kwargs,
            pip_install=pip_install,
            hide=hide,
            python_version=python_version,
            out_type=RunPythonOut,
        )
        self.node = "RunPython"

    @property
    def future(self) -> FutureRunPythonOut:  # type: ignore
        """
        Future reference to this node's output.

        https://guides.substrate.run/reference/run-python
        """
        return super().future  # type: ignore
