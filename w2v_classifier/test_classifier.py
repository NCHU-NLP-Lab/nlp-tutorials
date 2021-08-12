import unittest
from torch import optim
from torch.utils import data

from ex_classifier.a_sent2vec import *
from ex_classifier.b_dataloader import SentDataloader
from ex_classifier.c_model import SentClassifier
from ex_classifier.d_predict import sent_predictor


class TestSent2Vec(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(sent2vec(''), [])

    def test_sim(self):
        self.assertEqual(sent2vec('台灣').shape, sent2vec('中國').shape)

    def test_shape(self):
        self.assertEqual(sent2vec('台灣').shape[0], 250)


class TestDataloader(unittest.TestCase):

    def test_workable(self):
        batch = 2
        dataloader = SentDataloader('udicstm_for_dataloader.csv')
        dl = data.DataLoader(dataset=dataloader,
                             batch_size=batch,
                             shuffle=True)
        for d in dl:
            input_vec, target = d
            print(input_vec, target)


class TestModel(unittest.TestCase):

    def test_workable(self):
        batch = 2
        dataloader = SentDataloader('udicstm_for_dataloader.csv')
        dl = data.DataLoader(dataset=dataloader,
                             batch_size=batch,
                             shuffle=True)
        classifier = SentClassifier(250, 2)
        for d in dl:
            input_vec, target = d
            preducted, loss = classifier.forward(input_vec, target)
        print(preducted)
        print(loss)


class Overall(unittest.TestCase):

    def test_workable(self):
        batch = 20
        epoch = 10
        dataloader = SentDataloader('udicstm_for_dataloader.csv')
        classifier = SentClassifier(250, 2)
        optimizer = optim.SGD(classifier.parameters(), lr=0.01, momentum=0.9)
        for ep in range(epoch):
            dl = data.DataLoader(dataset=dataloader,
                                 batch_size=batch,
                                 shuffle=True)
            total_loss = 0
            for d in dl:
                input_vec, target = d
                optimizer.zero_grad()
                preducted, loss = classifier.forward(input_vec, target)
                loss.backward()
                optimizer.step()
                total_loss += loss
            print(total_loss / len(dl))


class Predict(unittest.TestCase):
    def test_function(self):
        self.assertTrue(isinstance(sent_predictor('這餐廳的送餐速度很快，服務也很好'), str))

    def test_example(self):
        self.assertTrue(sent_predictor('這餐廳的送餐速度很快，服務也很好') == 'positive')
        self.assertTrue(sent_predictor('這飯店服務很糟糕') == 'negative')

if __name__ == '__main__':
    unittest.main(verbosity=2)
