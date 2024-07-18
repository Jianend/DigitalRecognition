from flask import Flask, request, jsonify
from flask import Flask, render_template
from mod import predict_digit_from_array
app = Flask(__name__, static_folder="static")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    # 接收POST请求中的JSON数据
    data = request.get_json()

    # 检查数据是否是有效的二维数组
    if not isinstance(data, list) or not all(isinstance(row, list) for row in data):
        return jsonify({'error': 'Invalid input data'}), 400

    # 为了演示，我们将返回数组的第一个元素作为预测结果
    prediction = predict_digit_from_array(data)

    # 返回预测结果
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)