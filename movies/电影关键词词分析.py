"""
@Author  ：叶庭云
@Date    ：2020/10/2 11:40
"""
import pandas as pd
import collections
from wordcloud import WordCloud
import matplotlib.pyplot as plt



#读取文件的某一列
df = pd.read_csv('tmdb_5000_movies.csv')['keywords']

key_words_list = []
for item in df:
    item = eval(item)
    if item:     # 为空列表  滤掉
        # ['aftercreditsstinger', 'duringcreditsstinger']  这个词语频率比较高 但好像没啥意义  滤掉
        key_words_list.extend([x['name'] for x in item if x['name'] not in ['aftercreditsstinger', 'duringcreditsstinger']])

words_count = collections.Counter(key_words_list)
#s=" ".join(key_words_list) 

#print(words_count)

wc = WordCloud(
    background_color='white',
    max_words=2000,
    max_font_size=100,
    random_state=8,
)

wc.generate_from_frequencies(words_count)
#wc.generate(s)
plt.imshow(wc)
plt.axis('off')
plt.savefig('test_003.png')
plt.show()
