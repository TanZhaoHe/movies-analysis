# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 22:05:20 2022

@author: GD005
"""


import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# 读取数据
df = pd.read_excel('已清洗数据.xlsx')
# 提取电影时长  平均评分
run_time, rating_score = df['runtime'], df['vote_average']

# 设置中文显示
mpl.rcParams['font.family'] = 'SimHei'
# 设置图形显示风格
plt.style.use('ggplot')
# 设置大小  像素
plt.figure(figsize=(9, 6), dpi=100)
# 绘制散点图
plt.scatter(run_time, rating_score, c='purple')
plt.yticks(np.arange(0, 10.5, 1))
# 添加描述信息
plt.title('电影平均评分与电影时长的关系', fontsize=18, x=0.5, y=1.02)
plt.xlabel('电影时长(分钟)')
plt.ylabel('平均评分')
# 保存图片
plt.savefig('test_006.png')
# 显示图片
plt.show()