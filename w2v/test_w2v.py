"""Example unit tests for `w2v`

Important
=========

Do not modify the way in which the functions `sim` is imported.

"""

import unittest

# code should be importable
from ex_w2v.w2v import sim


class TestKCM(unittest.TestCase):
    """Test the `word2vec` function defined in `.hw.word2vec`.
    """

    test_word_list = ['台灣', '政府', '公司']

    def test_empty(self):
        self.assertEqual(sim(''), [])

    def test_notinlist(self):
        self.assertEqual(sim('KNFER'), [])

    def test_existwords(self):
        for word in self.test_word_list:
            self.assertEqual(len(sim(word)), 10)

    def test_isprob(self):
        for word in self.test_word_list:
            [self.assertTrue(0 <= float(sim(word)[i][1]) <= 1) for i in range(len(sim(word)))]

    def test_sort(self):
        # result should be sort by frequency in descending order
        for word in self.test_word_list:
            self.assertTrue(all(sim(word)[i][1] >= sim(word)[i + 1][1] for i in range(len(sim(word)) - 1)))

    def test_length(self):
        # one word result should be removed
        for word in self.test_word_list:
            self.assertTrue(len(sim(word)[0]) > 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
