from typing import Any, Callable, List, Tuple, Union


class ChainBase:
    """A class for chaining functions together in a pipeline.

    Methods:
        __call__: Executes the function pipeline with an initial input value.
        add_function: Adds a function to the function pipeline.
        map: Adds a map function to the function pipeline.
        filter: Adds a filter function to the function pipeline.
        enumerate: Adds an enumerate function to the function pipeline.
        zip: Adds a zip function to the function pipeline.
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
    
    def _apply_function(self, function: Callable[..., Any], input_value: Any, *args: Any, **kwargs: Any) -> Any:
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

        for i, (function, args, kwargs) in enumerate(self.functions):
            try:
                output_value = self._apply_function(function, output_value, *args, **kwargs)
            except Exception as e:
                print(f"Error occurred at function {function.__name__} with inputs:")
                print(f"Input {i}: {output_value}")
                print(f"Additional args: {args}")
                print(f"Additional kwargs: {kwargs}")
                raise e
        return output_value


class Chain_Functions(ChainBase):

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


class Chain(Chain_Functions):
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

