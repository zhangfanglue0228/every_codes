# 使用selenium python库中的webdrive对象爬取豆瓣电影数据并分析

## 爬取内容
爬取豆瓣Top250电影的前100条短评

## `crawler.py`
爬取数据，以excel形式保存至同一目录下的data文件夹

## `data_process.py`
对数据进行处理：电影平均星级和平均短评情感得分平均值

## `kmeans.py`
+ 通过处理后的数据调用sklearn中的kmeans聚类方法聚类
+ 调用plotly库可视化分类