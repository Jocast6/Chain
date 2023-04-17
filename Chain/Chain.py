from collections import namedtuple
from dataclasses import dataclass
from typing import Any, Callable, List, Tuple, Union
import numpy as np


def _filter(f: Callable):
    def apply(seq: Any):
        return list(filter(f, seq))

    return apply

def _map(f: Callable):
    def apply(seq: Any):
        return list(map(f, seq))

    return apply


class Chain:
    """A class for chaining functions together in a pipeline.

    Methods:
        __call__: Executes the function pipeline with an initial input value.
        add_function: Adds a function to the function pipeline.
    """

    def __init__(self, initial_input: Any = None) -> None:
        self.functions: List[Tuple[Callable[..., Any], Tuple[Any, ...], dict]] = []
        self.initial_input = initial_input

    def __call__(self, initial_input: Any = None) -> Any:
        """Executes the function pipeline with an initial input value.

        Args:
            initial_input: The initial input value for the function pipeline.

        Returns:
            The output value of the last function in the pipeline.
        """
        return self.run(initial_input)
    
    def pipe(self, function: Callable[..., Any], *args: Any, **kwargs: Any) -> 'Chain':
        """Adds a function to the function pipeline.

        Args:
            function: The function to add to the pipeline.
            *args: Positional arguments to pass to the function.
            **kwargs: Keyword arguments to pass to the function.

        Returns:
            The Chain object for method chaining.
        """
        self.functions.append((function, args, kwargs))
        return self
    
    def apply_function(self, function: Callable[..., Any], input_value: Any, *args: Any, **kwargs: Any) -> Any:
        """Applies a function to an input value.

        Args:
            function: The function to apply.
            input_value: The input value to the function.
            *args: Positional arguments to pass to the function.
            **kwargs: Keyword arguments to pass to the function.

        Returns:
            The output value of the function.
        """
        if isinstance(input_value, tuple):
            output_value = function(*input_value, *args, **kwargs)
        else:
            output_value = function(input_value, *args, **kwargs)
            if isinstance(output_value, tuple):
                output_value = tuple(output_value)
        return output_value
    
    def run(self, initial_input: Any = None) -> Any:
        """Executes the function pipeline with an initial input value.

        Args:
            initial_input: The initial input value for the function pipeline.

        Returns:
            The output value of the last function in the pipeline.
        """
        output_value = initial_input if initial_input is not None else self.initial_input
        if output_value is None:
            return self

        for function, args, kwargs in self.functions:
            output_value = self.apply_function(function, output_value, *args, **kwargs)
        return output_value

    def map(self, f):
        self.pipe(_map(f))
        return self

    def filter(self, f):
        self.pipe(_filter(f))
        return self

