from ПРОГРАММНАЯ_ИНЖЕНЕРИЯ.ПРАКТИКА.ФайловаяСистема_И_ПопулярныеФорматы_Zip_And_Json.Функции.ПреобразовываниеЧЧФ import human_read_format

X = [
    15000,          # 1
    1023,           # 2
    (2**10),        # 3
    ((2**20)-2**10),    # 4
    (2**20),        # 5
    ((2**30)-2**20),    # 6
    (2**30),        # 7
    8294388923      # 8
]

x = 0
a = ['15КБ', '1023Б', '1КБ', '1023КБ', '1МБ', '1023МБ', '1ГБ', '8ГБ']
test = []

for i in X:
    x += 1
    test.append(human_read_format(i))
x = 0
if a == test:
    print('Тестирование прошло успешно')
else:
    print('Что произошло?')
    for i in X:
        x += 1
        print("Что у тебя: ", x, human_read_format(i))
    print("Что надо: ", a)