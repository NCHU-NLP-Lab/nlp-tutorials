from torch.utils import data
from .a_sent2vec import sent2vec
from sklearn.preprocessing import LabelEncoder
import pickle
import csv

class SentDataloader(data.Dataset):
    def __init__(self, fpath):
        sample = []
        maxlen = 0

        # 使用 LabelEncoder 對 label 做 encoder
        le = LabelEncoder()     
        le_target = le.fit_transform('answers list')



        #將 question 與 target 合併成一筆資料
        for q, target in zip('questions list', 'le_target'):    
            input = sent2vec('')
            sample.append([input, target])



        # 將資料向量補齊至最大長度，使資料維度都一樣
        zero_vetor = torch.zeros(1,250)     
        for ele in sample:        
            while ele[0].size(0) < maxlen:
                ele[0] = torch.cat((ele[0], zero_vetor), 0)  
        
        self.sample = sample
        self.maxlen = maxlen

    def __len__(self):
        return len(self.sample)

    def __getitem__(self, idx):
        return self.sample[idx]
