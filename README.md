# Chain
The Git repository contains code for a Python class called Chain that implements functional programming operations such as mapping, filtering, and reducing on iterable objects. The class provides methods for chaining these operations together, allowing for the creation of complex pipelines that can be applied to data. The repository includes unit tests that demonstrate the functionality of the Chain class, including tests for mapping, filtering, zipping, enumerating, and sorting operations. The tests use a variety of input types, including lists and data classes, and compare the results to expected output. Overall, the repository provides a useful tool for developers who wish to implement functional programming concepts in their Python code

```python
    # you can define custom functions and add them to the pipeline using Chain.pipe
    def higher_order_function_with_two_outputs(x, f):
        # this function takes a list: x, and a function: f, as inputs
        y = list(map(f, x))
        return x, y

    def add(x, y):
        # this function takes two list: x, y
        output = []
        for i in range(len(x)):
            output.append(x[i] + y[i])

        return output

    random_numbers = [86, 42, 12, 20, 6, 87, 1, 80, 7, 43]

    # create an instance of the Chain class and add functions to pipeline
    pipeline = Chain()\
        .map(lambda x: x + 100)\
        .map(lambda x: x - 100)\
        .filter(lambda x: x % 2 == 0)\
        .pipe(higher_order_function_with_two_outputs, lambda x: x*2)\
        .pipe(add)\
            
    # don't like backslashes?
    pipeline = (Chain()
        .map(lambda x: x + 100)
        .map(lambda x: x - 100)
        .filter(lambda x: x % 2 == 0)
        .pipe(higher_order_function_with_two_outputs, lambda x: x*2)# additional parammeters to functions can be passed with the Chain.pipe
        .pipe(add))

    # run the function pipeline with an initial input
    result = pipeline(random_numbers)

    self.assertEqual([258, 126, 36, 60, 18, 240], result)
```

## Installation

To install the package locally, run the following command from the root directory (where `setup.py` is located):

```sh
pip install .
```

This will install the `chain` package and its dependencies so you can import and use it in your Python projects.

## Usage

To use the `chain` package, you can import the `Chain` class from the `chain` module in your Python code:

```python
from chain import Chain
```

You can then create an instance of the `Chain` class and use its methods to build and execute functional programming pipelines on your data.
