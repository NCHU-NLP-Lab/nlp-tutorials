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

    test_word_list = ['臺灣', '周杰倫', '韓國瑜', '中興大學', '肺炎']

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
        example_list = ['臺灣地區', '臺北', '高雄', '臺南', '臺灣人', '南臺灣', '宜蘭', '臺中', '新竹', '全臺']
        overlap = set([result[0] for result in sim('臺灣')]) & set(example_list)
        self.assertTrue(len(overlap) / 10 > 0.7)

        example_list = ['王力宏', '楊丞琳', '蕭敬騰', '林宥嘉', '江蕙', '王心凌', '庾澄慶', '羅志祥', '潘瑋柏', '陶喆']
        overlap = set([result[0] for result in sim('周杰倫')]) & set(example_list)
        self.assertTrue(len(overlap) / 10 > 0.7)

        example_list = ['柯文哲', '蘇貞昌', '謝長廷', '陳其邁', '陳菊', '連勝文', '馬英九', '朱立倫', '賴清德', '吳敦義']
        overlap = set([result[0] for result in sim('韓國瑜')]) & set(example_list)
        self.assertTrue(len(overlap) / 10 > 0.7)

        example_list = ['國立中興大學', '國立成功大學', '逢甲大學', '國立清華大學', '國立中山大學', '臺灣大學', '東海大學', '國立臺灣師範大學', '國立東華大學', '高雄醫學大學']
        overlap = set([result[0] for result in sim('中興大學')]) & set(example_list)
        self.assertTrue(len(overlap) / 10 > 0.7)

        example_list = ['疫情', '冠狀病毒', '流感', '非典型肺炎', '新冠', '中東呼吸綜合症', 'COVID', '間質性', 'SARS', '吸入性']
        overlap = set([result[0] for result in sim('肺炎')]) & set(example_list)
        self.assertTrue(len(overlap) / 10 > 0.7)

if __name__ == '__main__':
    unittest.main(verbosity=2)
