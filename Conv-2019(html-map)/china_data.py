import requests
import json

import pandas as pd

from pyecharts.charts import Map
from pyecharts import options

url1 = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
data = requests.post(url1).text
content1 = json.loads(json.loads(data)['data'])

temp_content = content1['areaTree'][0]['children']
china_data = {}

for i in temp_content:
    china_data[i['name']] = i['total']['confirm']

map = Map(options.InitOpts(width='1200px', height='600px', bg_color="#ffffff",page_title='中国疫情地图'))
map.add(
        series_name="累计确诊",  #标签名称
        data_pair=china_data.items(),   #传入数据
        is_map_symbol_show=False,  #不显示标记
        maptype='china',   #地图类型
        )
map.set_global_opts(title_opts=options.TitleOpts(title='中国新冠肺炎累计确诊图', pos_left='center'),
                    legend_opts=options.LegendOpts(is_show=True, pos_left='left', pos_top='60%'),
                    visualmap_opts=options.VisualMapOpts(max_=1100000,is_piecewise=True,
                    pieces = [
                        {"max": 100, 'color': '#ffeead', 'label': '100人以下'},
                        {"min": 100, "max": 500, 'color': '#f29c2b', 'label': '100~500人'},
                        {"min": 500, "max": 2000, 'color': '#d9534f', 'label': '500~2000人'},
                        {"min": 2000, "max": 5000, "color": '#F71E35', 'label': '1000~5000人'},
                        {"min": 5000, 'color': '#C00000', 'label': '5k人以上'}]
                    ))

#设置系列配置项
map.set_series_opts(label_opts=options.LabelOpts(is_show=False))  #不显示国家名
map.render('china_map.html')