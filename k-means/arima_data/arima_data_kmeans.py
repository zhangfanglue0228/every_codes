from random import sample
from collections import defaultdict
from math import sqrt

import numpy as np
import pandas as pd


def calc_distance(l1=[], l2=[]):
    '''计算两列表之间的欧式距离'''
    distance = 0
    for i in range(len(l1)):
        distance += (l1[i] - l2[i]) ** 2
    return sqrt(distance)


def load_file():
    '''加载文件'''
    data_dataframe = pd.read_excel('arima_data.xls')
    data_array = np.array(data_dataframe)
    data_set = data_array.tolist()
    for i in data_set:
        i.pop(0)
    return data_set


def update_center(data_set, class_list, k):
    center_samples = []
    feature_num = len(data_set[0])  # 特征维度
    class_dict = defaultdict(list)
    for class_num, feature in zip(class_list, data_set):
        class_dict[class_num].append(feature)
    for i in range(k):
        temps = class_dict[i]
        new_center = []
        for j in range(feature_num):
            sum = 0.0
            for temp in temps:
                sum = sum + temp[j]
            tem_num = round(sum/len(temps), 4)
            new_center.append(tem_num)
        center_samples.append(new_center)
    return center_samples


def kmeans(data_set, k):
    center_samples = sample(data_set, k)  # 从特征数据集中选取k个样本作为质点
    before_class = []  # 保存上一次分类的结果
    after_class = []  # 保存此次分类的结果
    while True:
        # 分类
        for feature in data_set:
            tem_distance = []
            for center_sample in center_samples:
                tem_distance.append(calc_distance(feature, center_sample))
            after_class.append(tem_distance.index(min(tem_distance)))

        if before_class == after_class:
            # 判断上次分类结果和此次分类结果是否相同，相同则结束循环
            break
        else:
            # 更新质点
            center_samples = update_center(data_set, after_class, k)
            before_class = after_class[:]
            after_class = []

    return after_class


def print_result(result, data_set):
    print(*list(zip(result, data_set)), sep='\n')


def main():
    k = int(input())
    features = load_file()
    result = kmeans(features, k)
    # print_result(result, features)
    sum = [0] * k
    for i in result:
        sum[i] += 1
    print(sum)


if __name__ == "__main__":
    main()
