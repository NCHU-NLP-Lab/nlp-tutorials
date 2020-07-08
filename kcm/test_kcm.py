"""Example unit tests for `kcm`

Important
=========

Do not modify the way in which the functions `sim` is imported.

"""

import unittest

# code should be importable
from hw.kcm import sim


class TestKCM(unittest.TestCase):
    """Test the `kcm` function defined in `.hw.kcm`.

    """

    def test_none(self):
        self.assertEqual(sim(), [])

    def test_empty(self):
        self.assertEqual(sim(''), [])

    def test_notinlist(self):
        self.assertEqual(sim('KNFER'), [])

    def test_case1(self):
        self.assertEqual(len(sim('蔡英文')), 10)


if __name__ == '__main__':
    unittest.main(verbosity=2)
