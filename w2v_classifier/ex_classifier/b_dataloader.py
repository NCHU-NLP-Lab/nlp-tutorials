from torch.utils import data

from .a_sent2vec import sent2vec


class SentDataloader(data.Dataset):
    def __init__(self, fpath):

        # Initialize path and transform dataset
        sample = []
        input = sent2vec('')
        target = 1
        sample.append([input, target])
        sample.append([input, target])
        sample.append([input, target])
        self.sample = sample

    def __getitem__(self, idx):

        # Return the data (e.g. sentence_vec and label)
        return self.sample[idx]

    def __len__(self):
        
        # Indicate the total size of the dataset
        return len(self.sample)