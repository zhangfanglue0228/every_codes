from math import sqrt
from random import randint

import matplotlib.pyplot as plt
import matplotlib.cm as cm
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
    return sum


def create_data_list(data_list):
    '''
    创建数据集
    '''
    for i in range(500):  # 随机生成500个点
        data = Data()
        data.append_feature(randint(1, 200))
        data.append_feature(randint(1, 200))
        data_list.append(data)


def calu_density(data_list, dc):
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


kind_num = int(input('分类数量：') or 3)
dc_num = float(input('截断距离：') or 100)

data_list = []
create_data_list(data_list)
calu_density(data_list, dc=dc_num)
calu_distance(data_list)

data_temp_list = sorted(data_list, key=lambda x: x.density + x.distance, reverse=True)

# 分类
for data in data_list:
    classification = []
    for i in range(kind_num):
        classification.append(distance(data, data_temp_list[i]))

    data.kind = classification.index(min(classification))

# 打印结果
colors = cm.rainbow(np.linspace(0, 1, kind_num))
ax = plt.subplot()
for data in data_list:
    x = data.features[0]
    y = data.features[1]
    ax.scatter(x, y, alpha=0.6, c=colors[data.kind])
plt.show()
