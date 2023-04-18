# Chain
The Git repository contains code for a Python class called Chain that implements functional programming operations such as mapping, filtering, and reducing on iterable objects. The class provides methods for chaining these operations together, allowing for the creation of complex pipelines that can be applied to data. The repository includes unit tests that demonstrate the functionality of the Chain class, including tests for mapping, filtering, zipping, enumerating, and sorting operations. The tests use a variety of input types, including lists and data classes, and compare the results to expected output. Overall, the repository provides a useful tool for developers who wish to implement functional programming concepts in their Python code

```python
        def higher_order_function_with_two_outputs(x, f):
            # this function takes a list: x, and a function: f, as inputs
            other_output = list(map(f, x))
            return x, other_output

        def add(x, y):
            # this function takes two list: x, y
            output = []
            for i in range(len(x)):
                output.append(x[i] + y[i])

            return output

        random_numbers = [86, 42, 12, 20, 6, 87, 1, 80, 7, 43]

        # create an instance of the Chain class and add functions to pipeline
        chain = Chain()\
            .map(lambda x: x + 100)\
            .map(lambda x: x - 100)\
            .filter(lambda x: x % 2 == 0)\
            .pipe(higher_order_function_with_two_outputs, lambda x: x*2)\ # additional parammeters to functions can be passed with the Chain.pipe
            .pipe(add)\
            
        # don't like backslashes?
        chain = (Chain()
            .map(lambda x: x + 100)
            .map(lambda x: x - 100)
            .filter(lambda x: x % 2 == 0)
            .pipe(higher_order_function_with_two_outputs, lambda x: x*2) # additional parammeter to functions can be passed
            .pipe(add))

        # run the function pipeline with an initial input
        result = chain(random_numbers)

        self.assertEqual([258, 126, 36, 60, 18, 240], result)
```
