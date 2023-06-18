import torch.nn as nn

class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        #make 3 neural ntw layers l1,l2,l3
        self.l1=nn.Linear(input_size, hidden_size)
        self.l2=nn.Linear(hidden_size, hidden_size)
        self.l3=nn.Linear(hidden_size, num_classes)
        self.relu=nn.ReLU() #ReLU is the activation function used for transforming the summed weighted input from the node into the activation of the node or output for that input.
        # The rectified linear activation function or ReLU for short is a piecewise linear function that will output the input directly if it is positive, otherwise, it will output zero. It has become the default activation function for many types of neural networks because a model that uses it is easier to train and often achieves better performance.

    def forward(self,x):
        #x variable is the output for the required layer
        out=self.l1(x)
        out=self.relu(out)
        out=self.l2(out)
        out=self.relu(out)
        out=self.l3(out)
        return out