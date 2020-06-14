import csv
import random
import datetime

import pandas as pd
import matplotlib.pyplot as plt

fn = 'data.csv'

# 生成随机数据
with open(fn, 'w') as fp:
    wr = csv.writer(fp, lineterminator='\n')
    wr.writerow(['days', 'Sales'])
    startDate = datetime.date(2017, 1, 1)

    for i in range(365):
        amount = 300 + i*5+random.randrange(100)
        wr.writerow([str(startDate), amount])
        startDate = startDate+datetime.timedelta(days=1)


df = pd.read_csv('data.csv', encoding='cp936')
df = df.dropna()

# 生成营业额折线图
plt.figure()
df.plot(x='days')
plt.xticks(rotation=30, fontsize=8)
plt.savefig('first.png')

# 按月统计，生成柱状图
plt.figure()
df1 = df[:]
df1 = df1.copy()
df1['month'] = df1['days'].map(lambda x: x[:x.rindex('-')])
df1 = df1.groupby(by='month', as_index=False).sum()
df1.plot(x='month', kind='bar')
plt.savefig('second.png')

# 查找涨幅最大的月份，写入文件maxMonth.txt
df2 = df1.drop('month', axis=1).diff()
m = df2['Sales'].nlargest(1).keys()[0]
with open('maxMonth.txt', 'w') as fp:
    fp.write(df1.loc[m, 'month'])


# 按季度统计，生成饼状图
plt.figure()
one = df[:3]['Sales'].sum()
two = df[3:6]['Sales'].sum()
three = df[6:9]['Sales'].sum()
four = df[9:12]['Sales'].sum()
plt.pie([one, two, three, four], labels=['one quarter',
                                         'two quarter',
                                         'three quarter',
                                         'four quarter'])
plt.savefig('third.png')
