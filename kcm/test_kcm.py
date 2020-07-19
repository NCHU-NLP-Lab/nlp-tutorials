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

    test_word_list = ['臺灣', '周杰倫', '韓國瑜', '中興大學', '肺炎']

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
        example_list = ['日本', '中國大陸', '分佈', '香港', '中國', '群島', '中華民國', '美國', '地區', '臺北市']
        overlap = set([result[0] for result in sim('臺灣')]) & set(example_list)
        self.assertTrue(len(overlap) / 10 > 0.7)

        example_list = ['專輯', '演唱會', '歌曲', '電影', '歌手', '世界', '臺灣', '音樂', '合作', '方文山']
        overlap = set([result[0] for result in sim('周杰倫')]) & set(example_list)
        self.assertTrue(len(overlap) / 10 > 0.7)

        example_list = ['高雄市', '國民黨', '候選人', '中國國民黨', '高雄', '市長', '總統', '總統候選人', '高雄市市長', '選舉']
        overlap = set([result[0] for result in sim('韓國瑜')]) & set(example_list)
        self.assertTrue(len(overlap) / 10 > 0.7)

        example_list = ['大學', '清華大學', '臺灣', '成功', '臺灣大學', '臺中', '法商學院', '性騷擾', '政治', '教授']
        overlap = set([result[0] for result in sim('中興大學')]) & set(example_list)
        self.assertTrue(len(overlap) / 10 > 0.7)

        example_list = ['疫情', '武漢', '新冠', '感染', '冠狀病毒', '因應', '事件', '治療', '逝世', '急性']
        overlap = set([result[0] for result in sim('肺炎')]) & set(example_list)
        self.assertTrue(len(overlap) / 10 > 0.7)


if __name__ == '__main__':
    unittest.main(verbosity=2)
