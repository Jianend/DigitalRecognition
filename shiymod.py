import torch
from sz import Net

# 定义和加载模型
model = Net()
model.load_state_dict(torch.load('xunian.pth'))
model.eval()

# 定义转换
# 注意：在这里定义转换可能并不适用，因为转换通常应用于图像而非数组。
# 如果你打算从图像路径预测，那么保留这里的转换逻辑是合理的。
# 但如果你只从数组预测，那么转换逻辑应移至相应的预测函数内。

def predict_digit_from_array(image_array):
    # 将数组转换为Tensor，并进行预处理
    tensor_data = torch.tensor(image_array, dtype=torch.float32).unsqueeze(0).unsqueeze(0)
    image_tensor = (tensor_data - 0.5) / 0.5  # 根据你的normalize变换进行归一化
    image_tensor = image_tensor.unsqueeze(0)  # 添加通道维度
    # image_tensor = image_tensor.unsqueeze(0)  # 添加批次维度

    # 使用模型预测
    with torch.no_grad():
        output = model(image_tensor)
        _, predicted = torch.max(output.data, 1)

    # 打印预测结果
    return predicted.item()

# 使用图片路径进行预测
# 假设你有一个名为my_image_array的28x28的二维数组

# # 调用预测函数并打印结果
# predicted_number = predict_digit_from_array(my_image_array)
# print("预测数字：", predicted_number)