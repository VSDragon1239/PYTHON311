import pandas as pd
import scipy as sp
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import statistics as stat

df = pd.read_csv('./Ресурсы/UScomments.csv', on_bad_lines='skip')
df.dropna()

data = df['video_id'].value_counts()

s = input('Введите id видео ')
print('Количество комментариев под видео с id = ', s, ': ', data.at[s], sep='')

count = df['video_id'].value_counts().size
print('Количество различных видео:', count)

status = '0'

df.insert(loc=len(df.columns), column = "Status", value = status)
