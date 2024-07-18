 # 数字识别网站

[![Build Status](https://travis-ci.org/yourusername/digit-recognition.svg?branch=master)](https://travis-ci.org/yourusername/digit-recognition)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 目录

- [简介](#简介)
- [功能](#功能)
- [技术栈](#技术栈)
- [安装与运行](#安装与运行)
- [数据集](#数据集)
- [模型](#模型)
- [贡献](#贡献)
- [许可证](#许可证)
- [致谢](#致谢)

## 简介

数字识别网站是一个基于深度学习的在线平台，旨在识别手写数字。用户可以通过在画布上绘制数字，然后利用训练好的神经网络模型进行预测。该网站提供了直观的用户界面和实时反馈，使用户能够测试并了解机器学习模型的预测能力。

## 功能

- 实时手写数字输入
- 即时识别并显示预测结果
- 保存和分享预测结果的能力
- 可视化神经网络预测的概率分布

## 技术栈

- **前端**: HTML5, CSS3, JavaScript, React.js
- **后端**: python, Flask,

## 安装与运行

### 前提条件
- Python (用于模型训练脚本)

### 安装

```bash
git clone https://github.com/Jianend/DigitalRecognition.git
cd DigitalRecognition.git
python app.py