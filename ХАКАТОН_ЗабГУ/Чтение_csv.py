try:
    with open('./Ресурсы/UScomments.csv', 'r', encoding='utf-8') as file:
        for line in file:
            print(line)
except Exception as e:
    print("An error occurred while reading the file:", e)