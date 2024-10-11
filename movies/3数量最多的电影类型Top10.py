# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 01:23:54 2022

@author: GD005
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# 读取数据
df = pd.read_excel('已清洗数据.xlsx')
# 有个别行提取类型时不是nan 但为空列表 再提取后为nan
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



# 将数据集按年份分组并求和，得出每个年份，各电影类型的电影总数,对于二维数组

#erwei,axis=1表示按行相加 , axis=0表示按列相加

genresdf = genre_year.groupby('year').sum()
#genresdf.sum(axis=0) 按行求和
genres_count = genresdf.sum(axis=0).sort_values(ascending=False)    # 升序

#可替换为
#genres_count =  genre_year.sum(axis=0).sort_values(ascending=False)    # 升序


# print(genres_count.index)
# print(genres_count.values)
colors = ['#FF0000', '#FF1493', '#00BFFF', '#9932CC', '#0000CD', '#FFD700', '#FF4500', '#00FA9A', '#191970',
              '#006400']
# 设置大小   像素
plt.figure(figsize=(12, 8), dpi=100)
# 设置中文显示
mpl.rcParams['font.family'] = 'SimHei'
plt.style.use('ggplot')
# 绘制t条形图  设置柱条的宽度和颜色,fanzhuang
plt.barh(genres_count.index[9::-1], genres_count.values[9::-1], height=0.6, color=colors[::-1])
plt.xlabel('电影数量', fontsize=12)
plt.ylabel('电影类型', fontsize=12, color='red')
plt.title('数量最多的电影类型Top10', fontsize=18, x=0.5, y=1.05)
plt.savefig('test_001.png')
plt.show()





