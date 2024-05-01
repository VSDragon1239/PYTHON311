import pandas as pd
import re

# Загрузка данных
df = pd.read_csv('./Ресурсы/UScomments.csv', on_bad_lines='skip')

# Предлоги и местоимения для удаления
prepositions = ['а', 'в', 'но', 'не', 'ни', 'к', 'во', 'об', 'обо', 'про', 'с', 'со']
pronouns = ['я', 'ты', 'вы', 'мы', 'он', 'она', 'они', 'оно']


# Функция для обработки комментариев
def process_comment(comment):
    # Преобразование комментария в строку
    comment = str(comment)

    # Приведение к нижнему регистру
    comment = comment.lower()

    # Удаление предлогов и местоимений
    words = comment.split()
    words = [word for word in words if word not in prepositions and word not in pronouns]

    # Удаление смайлов
    comment = ' '.join(words)
    comment = re.sub(r'[\U00010000-\U0010ffff]', '', comment)

    # Удаление дубликатов
    words = list(set(words))

    # Удаление всего, кроме букв
    words = [re.sub(r'[^а-яА-Яa-zA-Z]', '', word) for word in words]

    # Обратно в str
    comment = ' '.join(words)

    # Удаление всех пробелов
    comment = comment.replace(' ', '')

    return comment


# Применение функции к каждому комментарию
df['comment_text'] = df['comment_text'].apply(process_comment)

# Сохранение обработанных данных в новый CSV файл
df.to_csv('Обработанные_комментарии.csv', index=False)

print("Обработанные данные сохранены в 'processed_comments.csv'")
