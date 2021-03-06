#!/usr/bin/env python
# -*- coding:utf-8 -*- 
"""
@Time：2019/3/22
@Author: hhzjj
@Description：一些常用的参数
"""

trn_rate = 0.5      # 训练集所占比例
val_rate = 0.25      # 验证集所占比例

trn_file = '../data/train.csv'
val_file = '../data/valid.csv'
tst_file = '../data/test.csv'
batch_size = 512
epochs = 5
num_layer = 1       # LSTM层数

model_path = 'param_1layer.pkl'