import unittest
from Chain import Chain
import numpy as np
from dataclasses import dataclass


class Test_Chain(unittest.TestCase):
    def test_with_iterable(self):
        def higher_order_function_with_two_outputs(x, f):
            return x, list(map(f, x))

        def add(x, y):
            output = []
            for i in range(len(x)):
                output.append(x[i] + y[i])

            return output

        random_numbers = [86, 42, 12, 20, 6, 87, 1, 80, 7, 43]

        # create an instance of the Chain class
        chain = Chain()\
            .map(lambda x: x + 100)\
            .map(lambda x: x - 100)\
            .filter(lambda x: x % 2 == 0)\
            .pipe(higher_order_function_with_two_outputs, lambda x: x*2)\
            .pipe(add)\

        # run the function pipeline with an initial input
        result = chain(random_numbers)

        self.assertEqual([258, 126, 36, 60, 18, 240], result)


    def test_with_dataclass(self):

        @dataclass
        class random_numbers:
            name: str
            arr: list

        random_numbers_list = []
        for i in range(5):
            random_numbers_list.append(
                random_numbers(name=str(i), arr=np.array([86, 42, 12, 20, 6, 87, 1, 80, 7, 43]))
            )


        # create an instance of the Chain class
        chain = Chain()\
            .map(lambda d: random_numbers(name=d.name, arr = (d.arr + 100)))\
            .map(lambda d: random_numbers(name=d.name, arr = (d.arr - 100)))\
            .filter(lambda d: random_numbers(name=d.name, arr= (d.arr % 2 == 0)))

        # run the function pipeline with an initial input
        result = chain(random_numbers_list)

        self.assertEqual([86, 42, 12, 20,  6, 87,  1, 80,  7, 43], list(result[0].arr))
        self.assertTrue(isinstance(result[i], random_numbers))


if __name__ == '__main__':
    unittest.main()
