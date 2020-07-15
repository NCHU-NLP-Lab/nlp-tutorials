from torch.utils import data

from .a_sent2vec import sent2vec


class SentDataloader(data.Dataset):
    def __init__(self, fpath):
        sample = []
        input = sent2vec('')
        target = 1
        sample.append([input, target])
        sample.append([input, target])
        sample.append([input, target])
        self.sample = sample

    def __len__(self):
        return len(self.sample)

    def __getitem__(self, idx):
        return self.sample[idx]
