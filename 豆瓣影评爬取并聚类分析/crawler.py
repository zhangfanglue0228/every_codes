import time
import random
import re

import pandas as pd

from selenium import webdriver

driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")

url_list = []
movie_name_list = []
for i in range(10):
    num = i * 25
    url = "https://movie.douban.com/top250?start=" + str(num) + "&filter="
    driver.get(url)
    # 定位获取对应数据
    elem1 = driver.find_elements_by_xpath("//div[@class='info']/div[@class='hd']/a")
    elem2 = driver.find_elements_by_xpath("//div[@class='info']/div[@class='hd']/a/span[1]")
    for j in range(len(elem1)):
        url_list.append(elem1[j].get_attribute('href').encode('utf-8').decode('utf-8'))
        movie_name_list.append(elem2[j].text.encode('utf-8').decode('utf-8'))
    time.sleep(random.random() * 3)
    
with open('movies_name.txt', 'w', encoding='utf-8') as f:
    for movie_name in movie_name_list:
        f.write(movie_name + '\n')


movie_num_list = []
for url in url_list:
    temp = re.findall(r"\d+",url)
    movie_num_list.append(temp[0])

for i in range(len(movie_num_list)):
    movie_num = movie_num_list[i]
    movie_name = movie_name_list[i]

    data_list = []
    for i in range(0, 5):
        num = i*20
        url = "https://movie.douban.com/subject/" + movie_num + "/comments?start=" + str(num) + "&limit=20&sort=new_score&status=P"
        driver.get(url)
        #用户姓名
        elem1 = driver.find_elements_by_xpath("//div[@class='avatar']/a")  
        # 是否看过此电影
        elem2 = driver.find_elements_by_xpath("//span[@class='comment-info']/span[1]")
        #用户评分
        elem3 = driver.find_elements_by_xpath("//span[@class='comment-info']/span[2]")
        #有用数
        elem4 = driver.find_elements_by_xpath("//span[@class='comment-vote']/span[1]")
        #日期
        elem5 = driver.find_elements_by_xpath("//span[@class='comment-time ']")
        #评论
        elem6 = driver.find_elements_by_xpath("//span[@class='short']")

        for j in range(20):
            temp_list = []
            temp_list.append(elem1[j].get_attribute('title').encode('utf-8').decode('utf-8'))  # 用户名
            temp_list.append(elem2[j].text.encode('utf-8').decode('utf-8'))  # 是否看过此电影
            temp_list.append(elem3[j].get_attribute('class').encode('utf-8').decode('utf-8'))  # 评分
            temp_list.append(elem3[j].get_attribute('title').encode('utf-8').decode('utf-8'))  # 推荐度
            temp_list.append(elem4[j].text.encode('utf-8').decode('utf-8'))  # 有用数
            temp_list.append(elem5[j].text.encode('utf-8').decode('utf-8'))  # 评论日期
            temp_list.append(elem6[j].text.encode('utf-8').decode('utf-8'))  # 评论内容
            data_list.append(temp_list)

        time.sleep(random.random() * 3)


    user_data = pd.DataFrame(columns=['用户','是否看过此电影', '评分','推荐度','有用数','评论日期','评论内容'])
    for i in range(1, 101):
        user_data.loc[i] = data_list[i - 1]

    user_data.to_excel("data/" + movie_name + "影评数据.xlsx")