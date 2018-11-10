#import torch
import torch.nn as nn
#import numpy as np

action_size = 37

class Dueling_DQN(nn.Module):
    
    def __init__(self):
        
        super(Dueling_DQN, self).__init__()
        self.linear1 = nn.Linear(action_size, action_size)
        
        self.advantage1 = nn.Linear(action_size, action_size)
        self.advantage2 = nn.Linear(action_size, action_size)
        
        self.value1 = nn.Linear(action_size, action_size)
        self.value2 = nn.Linear(action_size, 1)

        #self.activation = nn.Tanh()
        self.activation = nn.ReLU()
        
        
    def forward(self, x):
        output1 = self.linear1(x)
        output1 = self.activation(output1)
        
        output_advantage = self.advantage1(output1)
        output_advantage = self.activation(output_advantage)
        output_advantage = self.advantage2(output_advantage)
        
        output_value = self.value1(output1)
        output_value = self.activation(output_value)
        output_value = self.value2(output_value)
        
        return (output_value + output_advantage - output_advantage.mean())