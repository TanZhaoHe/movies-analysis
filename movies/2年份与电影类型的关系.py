# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 00:23:11 2022

@author: GD005
"""

import json
import pandas as pd
import numpy as np
from datetime import datetime
import warnings
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns


# 读取Excel数据
df = pd.read_excel('已清洗数据.xlsx')
# 有个别行数据清洗时不是nan 但为空列表 提取后为nan
df.dropna(inplace=True)
# 建立genres列表，提取电影的类型
genres_set = set()
for genre in df['genres'].str.split('|'):
    for item in genre:
        genres_set.add(item)


genres_list = list(genres_set)

for genre in genres_list:
    # 判断每行  有这个类型  对应类型的列下添个1
    #使用了lambada函数
    df[genre] = df['genres'].str.contains(genre).apply(lambda x: 1 if x else 0)


#所有的行，列名是电影类型种类
genre_year = df.loc[:, genres_list]
# 将年份作为索引标签
genre_year.index = df['year']
# 将数据集按年份分组并求和，得出每个年份，各电影类型的电影总数
genresdf = genre_year.groupby('year').sum()
# 包含年份与电影类型数量的DataFrame
print(genresdf)
# 取2000-2016年的电影类型数量  热力图可视化 17年数据就没几部
datas = genresdf.iloc[-18:-1:1, ::]
mpl.rcParams['font.family'] = 'Kaiti'
fig, ax = plt.subplots(figsize=(15, 9))
print(datas)
# 绘制热力图    cmap：从数字到色彩空间的映射
sns.heatmap(data=datas.T,#转置
            linewidths=0.25,
            linecolor='white',
            ax=ax,
            annot=True,
            fmt='d',
            cmap='Accent', 
            robust=True,
            )

# 添加描述信息   x y轴  title
ax.set_xlabel('年份', fontdict={'size': 18, 'weight': 'bold'})
ax.set_ylabel('电影类型', fontdict={'size': 18, 'weight': 'bold'})
ax.set_title(r'2000-2016年各电影类型数量', fontsize=25, x=0.5, y=1.02)

# 隐藏边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# 保存 展示图片
plt.savefig('heat_map.png')
plt.show()
