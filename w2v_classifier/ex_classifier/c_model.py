import torch
from torch import nn


class SentClassifier(nn.Module):
    def __init__(self, input_dim, n_classes):
        super(SentClassifier, self).__init__()

        # dimensionalities
        self.input_dim = input_dim
        self.n_classes = n_classes
        self.hidden_dim = 500

        # creates a MLP
        self.classifier = nn.Sequential(
            nn.Linear(self.input_dim, self.hidden_dim),
            nn.Tanh(),
            nn.Linear(self.hidden_dim, self.n_classes))

    def forward(self, sentence_vec, target=None):
        
        predicted = torch.tensor([[0.9, 0.1]], requires_grad=True)
        predicted_value, predicted_class = torch.max(predicted, 1)

        if target is not None:
            criterion = nn.CrossEntropyLoss()
            loss = criterion(predicted, torch.tensor([0]))
            return predicted_class, loss
        else:
            return predicted_class
