"""Example unit tests for `kcm`

Important
=========

Do not modify the way in which the functions `sim` is imported.

"""

import unittest

# code should be importable
from ex_kcm.kcm import sim


class TestKCM(unittest.TestCase):
    """Test the `kcm` function defined in `.hw.kcm`.

    """

    test_word_list = ['臺灣', '蔡英文', '復仇者聯盟', '中興大學', '肺炎']

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
        example_list = ['配音', '香港', '大陸', '日本', '聲演', '日治', '中國大陸', '名稱', '傳統', '地域']
        overlap = set([result[0] for result in sim('臺灣')]) & set(example_list)
        self.assertTrue(len(overlap) / 10 > 0.7)

        example_list = ['總統', '中華民國總統', '民進黨', '主席', '臺灣', '民主進步黨', '時任', '競選', '馬英九', '總統府']
        overlap = set([result[0] for result in sim('蔡英文')]) & set(example_list)
        self.assertTrue(len(overlap) / 10 > 0.7)

        example_list = ['無限', '電影', '奧創', '紀元', '終局', '漫威', '英雄', '內戰', '美國隊長', '飾演']
        overlap = set([result[0] for result in sim('韓國瑜')]) & set(example_list)
        self.assertTrue(len(overlap) / 10 > 0.7)

        example_list = ['大學', '教授', '臺灣', '畢業', '臺灣省立', '農學院', '法商學院', '研究所', '合併', '師範大學']
        overlap = set([result[0] for result in sim('中興大學')]) & set(example_list)
        self.assertTrue(len(overlap) / 10 > 0.7)

        example_list = ['病例', '新冠', '冠狀病毒', '疫情', '傳染性', '報告', '感染', '武漢', '人數', '患者']
        overlap = set([result[0] for result in sim('肺炎')]) & set(example_list)
        self.assertTrue(len(overlap) / 10 > 0.7)


if __name__ == '__main__':
    unittest.main(verbosity=2)
