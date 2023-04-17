import unittest
from unittest import result
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

    def test_zip_function(self):
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        
        result = Chain()\
            .zip()\
            .map(lambda x: x[0] + x[1])

        self.assertEqual([5, 7, 9], result((list1, list2)))

    def test_zip_function_with_added_parameter(self):
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        
        result = Chain()\
            .zip(list2)\
            .map(lambda x: x[0] + x[1])

        self.assertEqual([5, 7, 9], result(list1))

    def test_enumerate_function(self):
        my_list = ['apple', 'banana', 'orange']

        result = Chain()\
            .enumerate()\
            .map(lambda i: f"{i[0]}: {i[1]}")

        self.assertEqual(['0: apple', '1: banana', '2: orange'], result(my_list))

    def test_map_function(self):
        my_list = [1, 2, 3, 4, 5]
        result = Chain()\
            .map(lambda x: x ** 2)\
            .run(my_list)

        self.assertEqual([1, 4, 9, 16, 25], result)

    def test_filter_function(self):
        my_list = [1, 2, 3, 4, 5]
        result = Chain()\
            .filter(lambda x: x % 2 == 0)\
            .run(my_list)
        self.assertEqual([2, 4], result)

    def test_sort(self):
        data = [4, 2, 3, 1, 5]
        expected_output = [1, 2, 3, 4, 5]
        result = Chain()\
            .sort()
        self.assertEqual(result(data), expected_output)


if __name__ == '__main__':
    unittest.main()
