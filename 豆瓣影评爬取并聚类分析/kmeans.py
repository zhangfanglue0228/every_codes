import numpy as np
import pandas as pd
import plotly.express as px


from plotly.offline import plot
from sklearn.cluster import KMeans

data = pd.read_excel("final_data.xlsx")[['平均星级', '情感分平均值']]

movie_names = []
with open('movies_name.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        movie_names.append(line.rstrip('\n'))

estimator = KMeans(n_clusters=3)  # 构造聚类器
estimator.fit(data)  # 聚类
label_pred = estimator.labels_  # 获取聚类标签

kind_data = pd.DataFrame(columns=['电影名称', '平均星级', '情感分平均值', '种类'])
kind_data['电影名称'] = movie_names
kind_data['平均星级'] = data['平均星级'].tolist()
kind_data['情感分平均值'] = data['情感分平均值'].tolist()
kind_data['种类'] = label_pred

fig = px.scatter(kind_data, x='平均星级', y='情感分平均值', color='种类',
                 hover_name='电影名称', size='平均星级', log_x=True)
plot(fig)