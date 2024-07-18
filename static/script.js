// 创建28x28的二维数组，初始化所有值为0
const gridArray = Array.from({length: 28}, () => Array(28).fill(0));

// 获取DOM中的grid容器
const gridContainer = document.getElementById('grid');
let dragging = false;

for (let row = 0; row < 28; row++) {
    for (let col = 0; col < 28; col++) {
        const cell = document.createElement('div');
        cell.className = 'cell';

        cell.addEventListener('mousedown', function() {
            dragging = true;
            changeCellColor(this, row, col);
        });

        cell.addEventListener('mouseup', function() {
            dragging = false;
        });

        cell.addEventListener('mouseover', function() {
            if (dragging) {
                changeCellColor(this, row, col);
            }
        });

        gridContainer.appendChild(cell);
    }
}

function changeCellColor(cell, row, col) {
    cell.style.backgroundColor = 'black';
    gridArray[row][col] = 1;
}
function SendArray(){
    // 将二维数组发送到后端
    // console.log(gridArray);

    // 发送请求到后端，获取结果并显示在页面上
    fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(gridArray)
    })
   .then(response => response.json())
   .then(data => {
        // console.log(data);
        const result = document.getElementById('result');
        result.innerHTML = `The predicted number is ${data.prediction}`;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
function empty(){
    // 将二维数组清空
    for (let row = 0; row < 28; row++) {
        for (let col = 0; col < 28; col++) {
            gridArray[row][col] = 0;
            const cell = document.querySelectorAll('.cell')[row * 28 + col];
            cell.style.backgroundColor = 'white';
        }
        const result = document.getElementById('result');
        result.innerHTML = '';
        dragging = false;
    }
}