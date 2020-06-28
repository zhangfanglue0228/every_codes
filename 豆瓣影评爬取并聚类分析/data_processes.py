import pandas as pd

import re

from snownlp import SnowNLP

movie_names = []
with open('movies_name.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        movie_names.append(line.rstrip('\n'))

star_ave = []
cotent_score_ave = []
for movie_name in movie_names:
    print(movie_names.index(movie_name))
    data = pd.read_excel(movie_name + "影评数据.xlsx")[['用户','是否看过此电影', '评分', '推荐度', '有用数', '评论日期', '评论内容']]
    
    temp = data['评分'].tolist()
    temp_list = []
    for i in temp:
        if i == 'comment-time ':
            temp_list.append(30)
        else:
            temp_list.append(int(re.findall(r'\d+', i)[0]))
    star_ave.append(sum(temp_list)/len(temp_list))

    temp = data['评论内容'].tolist()
    temp_list = []
    for i in temp:
        s = SnowNLP(str(i))
        temp_list.append(s.sentiments)
    cotent_score_ave.append(sum(temp_list)/len(temp_list))

final_data = pd.DataFrame(index=movie_names, columns=['平均星级', '情感分平均值'])
final_data['平均星级'] = star_ave
final_data['情感分平均值'] = cotent_score_ave
final_data.to_excel("final_data.xlsx")