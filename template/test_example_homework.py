"""Example unit tests for `example_homework`

Important
=========

Do not modify the way in which the functions `square` and `cube` are imported.
This will be exactly the way we import your code for use in grading. You are
encouraged to add as many additional tests as you like.

"""

import unittest

# code should be importable
from example_homework.squaring import square
from example_homework.cubing import cube


class TestSquare(unittest.TestCase):
    """Test the `square` function defined in `example_homework.square`.

    Test the basic properties of the `square` function. In particular, how it
    behaves on the numbers zero and one as well as some example numbers, both
    positive and negative.

    """

    def test_zero(self):
        self.assertEqual(square(0), 0)

    def test_one(self):
        self.assertEqual(square(1), 1)

    def test_two_three_four(self):
        self.assertEqual(square(2), 4)
        self.assertEqual(square(3), 9)
        self.assertEqual(square(4), 16)

    def test_negative(self):
        self.assertEqual(square(-1), 1)


class TestCube(unittest.TestCase):
    """Test the `cube` function defined in `example_homework.cube`.

    Test the basic properties of the `cube` function. In particular, how it
    behaves on the numbers zero and one as well as some example numbers, both
    positive and negative.

    """

    def test_zero(self):
        self.assertEqual(cube(0), 0)

    def test_one(self):
        self.assertEqual(cube(1), 1)

    def test_two_three_four(self):
        self.assertEqual(cube(2), 8)
        self.assertEqual(cube(3), 27)
        self.assertEqual(cube(4), 64)

    def test_negative(self):
        self.assertEqual(cube(-1), -1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
