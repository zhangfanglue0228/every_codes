from math import sqrt
from random import randint

import pandas as pd
import numpy as np


class Data():
    '''
    定义数据类
    '''
    def __init__(self):
        self.features = []
        self.density = 0  # 局部密度
        self.distance = 0  # 距离
        self.kind = None

    def append_feature(self, feature):
        self.features.append(feature)


def distance(data1, data2):
    '''
    计算两点间的欧氏距离
    '''
    sum = 0
    for i in range(len(data1.features)):
        sum = sum + (data1.features[i] - data2.features[i]) ** 2
    return sqrt(sum)


def load_file(data_list):
    '''加载文件'''
    data_dataframe = pd.read_excel('sales_data.xls')
    data_array = np.array(data_dataframe)
    data_set = data_array.tolist()
    for i in data_set:
        i.pop(0)
    data_dict = {
        "坏": 0,
        "好": 1,
        "是": 1,
        "否": 0,
        "高": 1,
        "低": 0,
    }
    for i in range(len(data_set)):
        for j in range(len(data_set[i])):
            data_set[i][j] = data_dict[data_set[i][j]]
    for elements in data_set:
            data = Data()
            for element in elements:
                data.append_feature(element)
            data_list.append(data)


def calu_density(data_list, dc=120):
    '''
    计算密度
    '''
    for data1 in data_list:
        for data2 in data_list:
            if distance(data1, data2) == 0:
                pass
            else:
                if distance(data1, data2) < dc:
                    data1.density += 1


def calu_distance(data_list):
    for data1 in data_list:
        flag = 1  # 假设是局部密度最大点
        distance_num = []
        for data2 in data_list:
            if data1.density < data2.density:
                flag = 0  # 不是局部密度最大点了
                distance_num.append(distance(data1, data2))
        if flag == 0:  # 不是局部密度最大点，
            data1.distance = min(distance_num)
        else:  # 是局部密度最大点
            for data2 in data_list:
                data1.distance = max(distance(data1, data2), data1.distance)


class_num = int(input('分类数量：'))

data_list = []
load_file(data_list)
calu_density(data_list, dc=80)
calu_distance(data_list)

data_temp_list = sorted(data_list, key=lambda x: x.density + x.distance, reverse=True)

# 分类
for data in data_list:
    classification = []
    for i in range(class_num):
        classification.append(distance(data, data_temp_list[i]))

    data.kind = classification.index(min(classification))

# 打印结果
num = [0, 0]
for data in data_list:
    num[data.kind] += 1

print(num)
