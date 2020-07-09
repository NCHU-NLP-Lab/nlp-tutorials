"""Example unit tests for `kcm`

Important
=========

Do not modify the way in which the functions `sim` is imported.

"""

import unittest

# code should be importable
from ex.kcm import sim


class TestKCM(unittest.TestCase):
    """Test the `kcm` function defined in `.hw.kcm`.

    """

    test_word_list = ['台灣', '政府', '公司']

    def test_empty(self):
        self.assertEqual(sim(''), [])

    def test_notinlist(self):
        self.assertEqual(sim('KNFER'), [])

    def test_existwords(self):
        for word in self.test_word_list:
            self.assertEqual(len(sim(word)), 10)

    def test_sort(self):
        # result should be sort by frequency in descending order
        for word in self.test_word_list:
            self.assertTrue(all(sim(word)[i][1] >= sim(word)[i + 1][1] for i in range(len(sim(word)) - 1)))

    def test_length(self):
        # one word result should be removed
        for word in self.test_word_list:
            self.assertTrue(len(sim(word)[0]) > 1)

    def test_example(self):
        example_list = ['政府', '核四', '政治', '事件', '盧碧', '周子瑜', '洪素珠', '林義雄', '日本', '林冠']
        overlap = set([result[0] for result in sim('台灣')]) & set(example_list)
        self.assertTrue(len(overlap) / 10 > 0.7)


if __name__ == '__main__':
    unittest.main(verbosity=2)
