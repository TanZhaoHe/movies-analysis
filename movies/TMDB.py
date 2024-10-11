# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 20:36:11 2022

@author: 10648
"""

import json
import pandas as pd
import numpy as np
from datetime import datetime
import warnings

warnings.filterwarnings('ignore')    # 不显示告警信息
# 读取电影数据  指定引擎  不然会报错误
df = pd.read_csv('tmdb_5000_movies.csv', engine='python')
df.head()
# 由于数据集中包含的信息过多，其中部分数据并不是我们研究的重点，所以从中抽取分析要用的数据：
# 关键词  电影名称  电影类型  首次上映日期  电影时长  预算  收入
df1 = df[['keywords', 'original_title', 'genres', 'release_date', 'runtime', 'budget', 'revenue', 'vote_count', 'vote_average']]
df1.info()

#缺失值查看
df1[df1.isnull().values==True]
#处理缺失值
#方法一 直接丢弃有缺失值的行
df2=df1.dropna(axis=0)
df2.info()
# 方法二  查阅资料 填充缺失数据
# IMDb官网  https://www.imdb.com/title/tt3856124/

df1.loc[2656, 'runtime'] = 98.0
df1.loc[4140, 'runtime'] = 81.0
df1.loc[4553, 'release_date'] = '2014-06-01'
df1.info()

# genres列数据处理
df1['genres'].head()
# 将str转换为json
df1['genres'] = df1['genres'].apply(json.loads)

def decode(col):
    genre = []
    for item in col:
        genre.append(item['name'])
    return '|'.join(genre)

df1['genres'] = df1['genres'].apply(decode)
df1.head()
# 提取release_date的年份,只提取年份
df1['release_date'] = pd.to_datetime(df1['release_date']).dt.year
# 改列的名称
col = {'release_date': 'year'}
df1.rename(columns=col, inplace=True)
df1['year'].apply(int).head()    # 转为整数
# 保存为已清洗数据
df1.to_excel('已清洗数据.xlsx')