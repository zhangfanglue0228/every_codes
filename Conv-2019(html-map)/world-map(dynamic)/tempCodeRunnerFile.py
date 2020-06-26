data['Confirmed'] = data['Confirmed'] - data['Recovered'] - data['Deaths']

# times = data['Date'].tolist()
# times = list(set(times))
# times.sort()

# countries = data['Country'].tolist()
# countries = list(set(countries))
# countries.sort()

# countries_data = defaultdict(list)
# for i in data.iterrows():
#     countries_data[i[1]['Country']].append(i[1]['Confirmed'])

# world_data = pd.DataFrame(columns=countries, index=times)
# for country in countries:
#     world_data[country] = countries_data[country]
#     # print(len(countries_data[country]))

# world_data.rename(columns={'US':'United States'}, inplace=True)
# world_data.rename(columns={'Congo (Kinshasa)':'Dem. Rep. Congo'}, inplace=True)
# world_data.rename(columns={'Congo (Brazzaville)':'Congo'}, inplace=True)
# world_data.rename(columns={'South Sudan':'S. Sudan'}, inplace=True)
# world_data.rename(columns={'Central African Republic':'Central African Rep.'}, inplace=True)
# world_data.rename(columns={'Western Sahara':'W. Sahara'}, inplace=True)
# world_data.rename(columns={'Laos':'Lao PDR'}, inplace=True)
# world_data.rename(columns={"Cote d'Ivoire":"Côte d'Ivoire"}, inplace=True)
# world_data.rename(columns={'Korea, South':'Korea'}, inplace=True)
# world_data.rename(columns={'Dominica':'Dominican Rep.'}, inplace=True)

# # world_data.to_excel('world_data.xlsx')  # 输出文件

# attr = world_data.columns.tolist()
# timeline = Timeline()
# for i in range(len(world_data)):
#     #取每日数据
#     row = world_data.iloc[i,].tolist()
#     #将数据转换为二元的列表
#     sequence_temp = list(zip(attr,row))
#     #对日期格式化以便显示
#     time = world_data.index[i]
#     #创建地图
#     map_temp =(
#         Map()
#         .add(time, sequence_temp, maptype="world", is_map_symbol_show=False)
#         .set_global_opts(
#             legend_opts=options.LegendOpts(is_show=True, pos_left='left', pos_top='50%'),
#             title_opts=options.TitleOpts(title="世界疫情现存确诊动态地图"),
#             visualmap_opts=options.VisualMapOpts(max_=51000),
#         )
#         .set_series_opts(label_opts=options.LabelOpts(is_show=False))
#     )
#     #将地图加入时间轴对象
#     timeline.add(map_temp,time).add_schema(play_interval=36)

# # 地图创建完成后，通过render()方法可以将地图渲染为html 
# timeline.render('世界疫情动态地图.html')
