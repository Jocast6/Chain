from typing import Any, Callable
from .ChainFunctional import ChainFunctional


class Chain(ChainFunctional):
    def map(self, f: Callable[..., Any]):
        """Adds a map function to the pipeline.
        Args:
            f: The function to apply to each element of the sequence.
        Returns:
            The Chain object for method chaining.
        """
        self.pipe(self._map(f))
        return self


    def filter(self, f: Callable[..., Any]):
        """Adds a filter function to the pipeline.
        Args:
            f: The function used to filter the sequence.
        Returns:
            The Chain object for method chaining.
        """
        self.pipe(self._filter(f))
        return self


    def enumerate(self, start=0):
        """Adds an enumerate function to the pipeline.
        Args:
            start: The start index of the enumeration.
        Returns:
            The Chain object for method chaining.
        """
        self.pipe(lambda *args: enumerate(*args, start=start))
        return self


    def zip(self, *iterables):
        """Adds a zip function to the pipeline.
        Args:
            *iterables: The iterable(s) to zip with the original sequence.
        Returns:
            The Chain object for method chaining.
        """
        self.pipe(self._zip(*iterables))
        return self

    def unpack(self, f: Callable[..., Any]):
        """Adds an unpacking function to the pipeline.
        Args:
            f: The function used to unpack a sequence.
        Returns:
            The Chain object for method chaining.
        """
        self.map(self._unpack(f))
        return self

    def sort(self, reverse=False):
        """
        Sort the current data set and update the current state.

        Args:
            key: A function to specify the sorting key.
            reverse: A boolean value to specify whether to sort in reverse order.

        Returns:
            The Chain object for method chaining.
        """
        self.pipe(lambda *args: sorted(*args, reverse=reverse))
        return self

