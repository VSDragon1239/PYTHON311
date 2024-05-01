import pandas as pd
import csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Загрузка данных
with open('./Ресурсы/UScomments.csv', 'r', encoding='utf-8') as file:
    data = pd.read_csv(file, delimiter='\t', quoting=csv.QUOTE_NONE)

# Использование TF-IDF для преобразования текстовых данных в числовые данные
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(data['comment_text'])

# Применение алгоритма K-means
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)

# Добавление меток кластеров в исходные данные
data['cluster'] = kmeans.labels_

# Разделение данных на полезные и менее полезные комментарии
useful_comments = data[data['cluster'] == 0]
less_useful_comments = data[data['cluster'] == 1]

