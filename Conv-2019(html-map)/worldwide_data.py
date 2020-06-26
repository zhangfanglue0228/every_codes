import requests
import json

import pandas as pd

from data import country_en_zh
from pyecharts.charts import Map
from pyecharts import options


world_data = {}

url1 = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
data = requests.post(url1).text
content1 = json.loads(json.loads(data)['data'])
world_data['中国'] = content1['chinaTotal']['confirm']


url2 = 'https://api.inews.qq.com/newsqa/v1/automation/foreign/country/ranklist'
data = requests.post(url2).text
content2 = json.loads(data)['data']
for data in content2:
    world_data[data['name']] = data['confirm']


map = Map(options.InitOpts(width='1200px', height='600px', bg_color="#ffffff",page_title='世界疫情地图'))
map.add(
        series_name="累计确诊",  #标签名称
        data_pair=world_data.items(),   #传入数据
        is_map_symbol_show=False,  #不显示标记
        maptype='world',   #地图类型
        name_map=country_en_zh
        )
map.set_global_opts(title_opts=options.TitleOpts(title='世界新冠肺炎累计确诊图', pos_left='center'),
                    legend_opts=options.LegendOpts(is_show=True, pos_left='left', pos_top='60%'),
                    visualmap_opts=options.VisualMapOpts(max_=1100000,is_piecewise=True,
                    pieces = [
                        {"max": 1000, 'color': '#ffeead', 'label': '1k人以下'},
                        {"min": 1000, "max": 50000, 'color': '#f29c2b', 'label': '1k~5w人'},
                        {"min": 50000, "max": 200000, 'color': '#d9534f', 'label': '5w-20w人'},
                        {"min": 200000, "max": 1000000, "color": '#F71E35', 'label': '20w-100w人'},
                        {"min": 1000000, 'color': '#C00000', 'label': '100w以上'}]
                    ))

#设置系列配置项
map.set_series_opts(label_opts=options.LabelOpts(is_show=False))  #不显示国家名
map.render('worldwide_map.html')  