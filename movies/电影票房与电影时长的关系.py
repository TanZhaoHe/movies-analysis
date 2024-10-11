 # -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 01:27:27 2022

@author: GD005
"""

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

# 读取数据
df = pd.read_excel('已清洗数据.xlsx')
# 电影时长   票房
run_time, revenue = df['runtime'], df['revenue']

# 设置中文显示
mpl.rcParams['font.family'] = 'SimHei'
# 设置图形显示风格
plt.style.use('ggplot')
# 设置大小  像素
plt.figure(figsize=(9, 6), dpi=100)
# 绘制散点图
plt.scatter(run_time, revenue)
# 添加描述信息
plt.title('电影票房与电影时长的关系', fontsize=18, x=0.5, y=1.02)
plt.xlabel('电影时长(分钟)')
plt.ylabel('电影票房(亿美元)')
# 保存图片
plt.savefig('test_005.png')
# 显示图片
plt.show()


