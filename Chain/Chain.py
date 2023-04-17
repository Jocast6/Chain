from typing import Any, Callable, List, Tuple, Union


class Chain(ChainFunctional):
    def map(self, f: Callable[..., Any]) -> 'Chain':
        """Adds a map function to the pipeline.
        Args:
            f: The function to apply to each element of the sequence.
        Returns:
            The Chain object for method chaining.
        """
        self.pipe(self._map(f))
        return self


    def filter(self, f: Callable[..., Any]) -> 'Chain':
        """Adds a filter function to the pipeline.
        Args:
            f: The function used to filter the sequence.
        Returns:
            The Chain object for method chaining.
        """
        self.pipe(self._filter(f))
        return self


    def enumerate(self) -> 'Chain':
        """Adds an enumerate function to the pipeline.
        Args:
            start: The start index of the enumeration.
        Returns:
            The Chain object for method chaining.
        """
        self.pipe(lambda *args: enumerate(*args))
        return self


    def zip(self, *iterables) -> 'Chain':
        """Adds a zip function to the pipeline.
        Args:
            *iterables: The iterable(s) to zip with the original sequence.
        Returns:
            The Chain object for method chaining.
        """
        self.pipe(lambda *args: zip(*args, *iterables))
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

