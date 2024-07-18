import torch
from torch import nn

# 打印输入张量x经过每一层时的维度变化
def print_shape(model,x):

    print(f"x: {x.shape}")
    x=  x.view(-1,28*28)
    print(f"after view: {x.shape}")
    x= model.layer1(x)
    print(f"after layer1: {x.shape}")
    x=torch.relu(x)
    print(f"after relu: {x.shape}")
    x= model.layer2(x)
    print(f"after layer2: {x.shape}")



    return x

# 手动遍历模型的各个结构，并计算参数数量
def count_parameters(model):
    # 打印层的名称和参数数量
    for name, param in model.named_parameters():
        if param.requires_grad:
            print(name, param.numel())
    return sum(p.numel() for p in model.parameters() if p.requires_grad)


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.layer1 = nn.Linear(28*28,256)
        self.layer2 = nn.Linear(256,10)
    def forward(self, x):
        x=x.view(-1,28*28)
        x=self.layer1(x)
        x=torch.relu(x)
        return self.layer2(x)

if __name__ == '__main__':
    net = Net()
    print(net)
    print(count_parameters(net))
    print_shape(net,torch.zeros(5,28,28)) 