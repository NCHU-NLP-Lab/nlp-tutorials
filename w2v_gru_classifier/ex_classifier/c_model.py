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
        self.gru_s2v = nn.GRU(self.input_dim, self.hidden_dim, batch_first=True)
        self.acf = nn.ReLU()
        self.classifier = nn.Linear(self.hidden_dim, self.n_classes)

    def forward(self, sentence_vec, target=None):
        
        h0 = torch.zeros(1, 100, 100)       # 初始化 hidden state (num_layers (GRU 層數), batch_size, hidden_dim)
        
        gru_output, hidden = self.gru_s2v(input, h0)     # 使用 gru 產生句向量
        
        gru_output = self.acf()     # 將 gru_output 最後一層向量經過 acf

        predicted = self.classifier()     # 丟入 linear layer 做分類
        
        predicted_value, predicted_class = torch.max(predicted, 1)

        if target is not None:
            criterion = nn.CrossEntropyLoss()
            loss = criterion(predicted, torch.tensor([0]))      # predicted 與 target 做 loss 計算
            return predicted_class, loss
        else:
            return predicted_class