from typing import Any, Callable

from .ChainBase import ChainBase


class ChainFunctional(ChainBase):

    @staticmethod
    def _filter(f: Callable):
        def apply(seq: Any):
            return list(filter(f, seq))

        return apply

    @staticmethod
    def _map(f: Callable):
        def apply(seq: Any):
            return list(map(f, seq))

        return apply

