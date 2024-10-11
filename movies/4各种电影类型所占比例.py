# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 22:56:30 2022

@author: GD005
"""


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

df = pd.read_excel('已清洗数据.xlsx')
# 有个别行提取类型时不是nan 但为空列表 提取后为nan
df.dropna(inplace=True)
# 建立genres列表，提取电影的类型
genres_set = set()
for genre in df['genres'].str.split('|'):
    for item in genre:
        genres_set.add(item)

genres_list = list(genres_set)

for genre in genres_list:
    # 判断每行  有这个类型  对应类型的列下添个1
    df[genre] = df['genres'].str.contains(genre).apply(lambda x: 1 if x else 0)
genre_year = df.loc[:, genres_list]


# 将年份作为索引标签
genre_year.index = df['year']


# 将数据集按年份分组并求和，得出每个年份，各电影类型的电影总数
genresdf = genre_year.groupby('year').sum()
genres_count = genresdf.sum(axis=0).sort_values(ascending=False)    # 升序
# print(genres_count.index)
# print(genres_count.values)
# print(len(genres_count.values))

# 设置中文显示
mpl.rcParams['font.family'] = 'SimHei'
# 设置大小  像素
plt.figure(figsize=(12, 8), dpi=100)
plt.axes(aspect='equal')   # 保证饼图是个正圆
explodes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1, 0.25, 0.4, 0.55, 0.7, 0.85]

#genres_count.values只是数值部分
plt.pie(genres_count.values, labels=genres_count.index,
     autopct='%.2f%%', shadow=True, explode=explodes,
  startangle=15, labeldistance=1.1,
  )
plt.title('各种电影类型所占比例', fontsize=18)
plt.savefig('test_002.png')
plt.show()