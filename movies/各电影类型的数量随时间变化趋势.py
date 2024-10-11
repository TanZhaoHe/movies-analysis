"""
@Author  ：叶庭云
@Date    ：2020/10/2 11:40
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# 读取数据
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
print(genresdf)
# 设置中文显示
mpl.rcParams['font.family'] = 'SimHei'
# 设置大小  像素
plt.figure(figsize=(10, 6), dpi=100)
# 设置图形显示风格
plt.style.use('ggplot')
# DataFrame 绘制折线图
plt.plot(genresdf, label=genresdf.columns)
# 添加描述信息
plt.xticks(range(1915, 2018, 5))
plt.xlabel('年份', fontsize=12)
plt.ylabel('电影数量', fontsize=12)
plt.title('各电影类型的数量随时间变化趋势', fontsize=18, x=0.5, y=1.02)
# 显示图例
plt.legend(genresdf)
# 保存图片
plt.savefig('test_004.png')
# 展示图片
plt.show()