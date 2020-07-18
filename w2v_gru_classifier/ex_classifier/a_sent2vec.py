import torch
from torch import nn


def sent2vec(sent=''):
    """
    Parameters
    ----------
    sent : string
        sentence
    Returns
    -------
    sentence_vector : torch.FloatTensor
        sentence vector from word vector, formatting in torch.tensor
    """
    inputs = torch.tensor([[1.0, 2.0, 3.0]])
    inputs = torch.cat(inputs).view(len(inputs), 1, -1)
    return inputs
