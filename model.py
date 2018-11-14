import torch
import torch.nn as nn
import torch.nn.functional as F

class QNetwork(nn.Module):

    """Class for neural network

    Attributes:
        state_size (int): Dimension of each state
        action_size (int): Dimension of each action
        seed (int): Random seed
    """

    def __init__(self, state_size, action_size, seed):
        """Initialize parameters and model architecture"""
        super(QNetwork, self).__init__()
        self.seed = torch.manual_seed(seed)
        self.fc1 = nn.Linear(state_size, 64)
        self.bn1=nn.BatchNorm1d(64)
        self.fc2 = nn.Linear(64,128)
        self.bn2=nn.BatchNorm1d(128)
        self.fc3 = nn.Linear(128,64)
        self.bn3=nn.BatchNorm1d(64) 
        self.fc4 = nn.Linear(64,32)
        self.bn4=nn.BatchNorm1d(32)
        self.al = nn.Linear(32, action_size)
        self.v=nn.Linear(32,1)
      

    def forward(self, state):
        """Forward propagation of neural network
        Args:
            state (vector): sized (self.state_size x batch size) with environment state data

        Returns:
            Vector sized (self.action_size x batch size) with return of a neural netowrk
        """

        x = F.relu(self.bn1(self.fc1(state)))
        x = F.relu(self.bn2(self.fc2(x)))
        x = F.relu(self.bn3(self.fc3(x)))
        x = F.relu(self.bn4(self.fc4(x)))
        value=self.v(x)
        af = self.al(x)
        x=value+(af-torch.mean(af))

        return x