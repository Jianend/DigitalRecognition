import torch
from torch import nn
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from sz import Net

# 数据预处理
transform = transforms.Compose([transforms.ToTensor(), 
                                transforms.Normalize((0.5,), (0.5,))])

# 加载MNIST数据集
trainset = datasets.MNIST('./pytorch/MNIST_data/', download=True, train=True, transform=transform)
trainloader = DataLoader(trainset, batch_size=64, shuffle=True)

testset = datasets.MNIST('./pytorch/MNIST_data/', download=True, train=False, transform=transform)
testloader = DataLoader(testset, batch_size=64, shuffle=True)

# 定义模型
model = Net()

# 定义损失函数和优化器
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# 训练模型
epochs = 50
for e in range(epochs):
    running_loss = 0
    for images, labels in trainloader:
        # 前向传播
        optimizer.zero_grad()
        output = model(images)
        
        # 计算损失
        loss = criterion(output, labels)
        
        # 反向传播
        loss.backward()
        
        # 更新权重
        optimizer.step()
        
        running_loss += loss.item()
    else:
        print(f"Training loss: {running_loss/len(trainloader)}")

# 评估模型
correct = 0
total = 0
with torch.no_grad():
    for images, labels in testloader:
        outputs = model(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print(f'Accuracy of the network on the 10000 test images: {100 * correct // total} %')
# 保存模型
torch.save(model.state_dict(), 'xunian.pth')
