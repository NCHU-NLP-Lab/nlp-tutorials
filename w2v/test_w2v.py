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

    test_word_list = ['臺灣', '蔡英文', '復仇者聯盟', '中興大學', '肺炎']

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

    def test_example(self):
        example_list = ['臺灣地區', '臺北', '南臺灣', '臺灣人', '高雄', '宜蘭', '臺南', '臺中', '新竹', '全臺']
        overlap = set([result[0] for result in sim('臺灣')]) & set(example_list)
        self.assertTrue(len(overlap) / 10 >= 0.5)

        example_list = ['馬英九', '陳水扁', '李登輝', '蘇貞昌', '韓國瑜', '柯文哲', '吳敦義', '宋楚瑜', '賴清德', '謝長廷']
        overlap = set([result[0] for result in sim('蔡英文')]) & set(example_list)
        self.assertTrue(len(overlap) / 10 >= 0.5)

        example_list = ['鋼鐵人', 'X戰警', '正義聯盟', '奧創', '美國隊長', '驚奇隊長', '戰警', '蜘蛛人', '水行俠', '奇異博士']
        overlap = set([result[0] for result in sim('復仇者聯盟')]) & set(example_list)
        self.assertTrue(len(overlap) / 10 >= 0.5)

        example_list = ['國立中興大學', '國立成功大學', '逢甲大學', '國立陽明大學', '國立中正大學', '國立屏東科技大學', '東海大學', '國立清華大學', '國立宜蘭大學', '靜宜大學']
        overlap = set([result[0] for result in sim('中興大學')]) & set(example_list)
        self.assertTrue(len(overlap) / 10 >= 0.5)

        example_list = ['COVID', '流感', '疫情', '冠狀病毒', '傳染性', '非典型肺炎', '新冠', '流行性感冒', '吸入性', 'Covid']
        overlap = set([result[0] for result in sim('肺炎')]) & set(example_list)
        self.assertTrue(len(overlap) / 10 >= 0.5)

if __name__ == '__main__':
    unittest.main(verbosity=2)
