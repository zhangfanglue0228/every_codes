import requests as rq
import re
import numpy as np
import pandas as pd
import requests
import json
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker
# 数据来源：新华网http://my-h5news.app.xinhuanet.com/h5activity/yiqingchaxun/index.html
url = 'http://fms.news.cn/swf/2020_sjxw/2_1_xgyq/js/data.js'
# 网页数据
home_rt = rq.get(url).text
# 提取日期
dates = re.search('_g_map_data_days = \[(.*?)\]', home_rt).group(1)
dates = re.findall('\'(.*?)\'', dates)
# 提取省份
provinces = re.search('_g_map_data_province = \[(.*?)\];', home_rt).group(1)
provinces = re.findall('\'(.*?)\'', provinces)
# 提取数据
data = re.search('_g_map_data_data =\[(.*?)\];', home_rt, re.S).group(1)
data = re.findall('\[(.*?)\]', data, re.S)
data = [i.split(',') for i in data]
data = np.array(data).T
# 生成表格
data = pd.DataFrame(data, columns=dates, index=provinces)
data = data.astype('int')  # 转换str类型为int型
last_colum = data.columns[-1]
data = data.sort_values(last_colum, ascending=False)
data.to_excel('china_data.xlsx')