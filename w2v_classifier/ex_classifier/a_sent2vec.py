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
    return torch.tensor([1.0, 2.0, 3.0])
