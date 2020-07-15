import unittest
from torch.utils import data

from ex_classifier.a_sent2vec import *
from ex_classifier.b_dataloader import SentDataloader
from ex_classifier.c_model import SentClassifier


class TestSent2Vec(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(sent2vec(''), None)

    def test_sim(self):
        self.assertEqual(sent2vec('台灣').shape, sent2vec('台灣').shape)

    def test_shape(self):
        self.assertEqual(sent2vec('台灣').shape[0], 1)


class TestDataloader(unittest.TestCase):

    def test_workable(self):
        batch = 2
        dataloader = SentDataloader('udicstm_for_dataloader.csv')
        dl = data.DataLoader(dataset=dataloader,
                             batch_size=batch,
                             shuffle=True)
        for i in dl:
            print(i)


class TestModel(unittest.TestCase):

    def test_workable(self):
        batch = 2
        dataloader = SentDataloader('path')
        dl = data.DataLoader(dataset=dataloader,
                             batch_size=batch,
                             shuffle=True)
        classifier = SentClassifier(3, 2)
        preducted, loss = classifier.forward(dl)
        print(preducted)
        print(loss)


class Overall(unittest.TestCase):

    def test_workable(self):
        batch = 2
        epoch = 10
        dataloader = SentDataloader('path')
        dl = data.DataLoader(dataset=dataloader,
                             batch_size=batch,
                             shuffle=True)
        classifier = SentClassifier(3, 2)
        for d in dl:
            preducted, loss = classifier.forward(d)
            loss.mean().backward()
            print(loss)


if __name__ == '__main__':
    unittest.main(verbosity=2)
