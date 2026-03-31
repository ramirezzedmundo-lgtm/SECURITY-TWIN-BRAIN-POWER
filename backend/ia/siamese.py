import torch
import torch.nn as nn

class SiameseNet(nn.Module):
    def __init__(self):
        super(SiameseNet, self).__init__()
        self.fc1 = nn.Linear(128, 64)
        self.fc2 = nn.Linear(64, 32)
        self.activation = nn.ReLU()

    def forward_once(self, x):
        x = self.activation(self.fc1(x))
        return self.fc2(x)

    def forward(self, input1, input2):
        output1 = self.forward_once(input1)
        output2 = self.forward_once(input2)
        return torch.abs(output1 - output2)
