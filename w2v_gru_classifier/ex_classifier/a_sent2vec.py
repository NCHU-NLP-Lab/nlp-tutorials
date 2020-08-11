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
    example
    -------    
    I love you.
    =>
        tensor([
         [1.0765e-01, -3.6939e+00,  1.2139e+00, -1.0561e+00, -2.0084e+00,       # "I" vector
          -1.4055e+00, -9.0298e-01, -2.3618e-01,  1.5151e+00, -1.2158e-01,
          2.3321e+00, -5.7944e-01, -2.2252e-01, ...],
         [-6.3879e-01, -1.7294e+00,  1.1637e-01, -1.0025e+00, -6.6298e-01,      # "love" vector
          -1.6146e+00, -1.1563e+00, -1.4284e+00,  1.1772e+00, -1.4051e+00,
          -5.2077e-01, -4.0171e-01, -1.9743e-01, ...],
         [4.7850e-01, -1.4013e+00, -7.7003e-01, -9.6428e-01, -6.0314e-01,       # "you" vector
          1.7834e-01,  6.1909e-02, -2.0041e-01,  4.4003e-01,  5.2138e-01,
          -2.2191e-01, -2.6324e-02, -1.1932e+00, ...]
        ])
    =>
        torch.Size([3,250]) #[keywords num, word2vec dim]
    """
    inputs = torch.tensor([[1.0, 2.0, 3.0]])
    inputs = torch.cat(inputs)     # torch.cat 合併向量
    inputs = torch.view(len(inputs), 250)       #torch.view 依指定數字做組合
    return inputs
