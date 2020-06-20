import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
# import json


base_data = [random.randint(-1000000000, 1000000000) for _ in range(500)]

k = int(input())
dist = {}

sample_list = random.sample(base_data, k)
before_ave = sample_list[:]
after_ave = []
while True:
    for i in range(k):
        dist[i] = []
    for data in base_data:
        data_dis = [(data - sample_data) ** 2 for sample_data in before_ave]
        min_subscript = data_dis.index(min(data_dis))
        dist[min_subscript].append(data)

    for key in dist:
        after_ave.append(np.mean(dist[key]))

    if after_ave == before_ave:
        break

    before_ave = after_ave[:]
    after_ave = []

# beautiful_format = json.dumps(dist, indent=4, ensure_ascii=False)
# print(beautiful_format)

color = ['red', 'blue' 'green', 'black', 'pink', 'orangered', 'teal']
colors = cm.rainbow(np.linspace(0, 1, k))

for key in dist:
    y = []
    for i in range(len(dist[key])):
        y.append(0)
    # print(len(dist[key]), len(y))
    plt.scatter(dist[key], y, c=colors[key], s=1.0)
    plt.xlim(-1100000000, 1100000000)
    plt.ylim(-1, 1)
plt.show()
