from typing import Any, Callable

from .ChainBase import ChainBase


class ChainFunctional(ChainBase):

    @staticmethod
    def _filter(f: Callable):
        def apply_filter(seq: Any):
            return list(filter(f, seq))

        return apply_filter

    @staticmethod
    def _map(f: Callable):
        def apply_map(seq: Any):
            return list(map(f, seq))

        return apply_map

    @staticmethod
    def _zip(*iterables):
        def apply_zip(*seq):
            return list(zip(*seq, *iterables))

        return apply_zip

    @staticmethod
    def _unpack(f: Callable):
        def unpacked(seq):
            return f(*seq)

        return unpacked

