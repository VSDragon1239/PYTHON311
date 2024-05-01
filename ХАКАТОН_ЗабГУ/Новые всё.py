import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import re
# from pycaret import clustering
from sklearn.datasets import make_blobs


mpl.rcParams['figure.dpi'] = 300

prepositions = ['а', 'в', 'но', 'не', 'ни', 'к', 'во', 'об', 'обо', 'про', 'с', 'со', 'и', 'на']
pronouns = ['я', 'ты', 'вы', 'мы', 'он', 'она', 'они', 'оно']


def file(data):
    count = data['video_id'].value_counts().size
    print('Количество различных видео в файле:', count)
    print('id видео:', df['video_id'].unique())


def comm_process(comment):
    comment = str(comment)
    comment.lower() # в нижний регистр
    words = comment.split()
    words = [word for word in words if word not in prepositions and word not in pronouns] # удалили предлоги и местоимения
    words = str(set(words))
    words = [re.sub(r'[^а-яА-Яa-zA-Z]', '', word) for word in words]
    new_comm = ''.join(words)
    return new_comm


def smile_process():
    pass


df = pd.read_csv('./Ресурсы/UScomments.csv', on_bad_lines='skip')
df.dropna()


data = df.head(10)
data['comment_text'] = data['comment_text'].apply(comm_process)

s = input('Введите id видео ')
print('Количество комментариев под видео с id = ', s, ': ', data[[s]][0], sep='')


status = '0'
df.insert(loc=len(df.columns), column="Status", value=status)


