
def human_read_format(size):
    size = int(size)
    X = 10
    if check_size(size) == 0:
        if size < 2**X:
            return str(size) + "Б"  # Байты
        elif size < 2**(X*2):
            return str(round((size/(2**X)))) + "КБ"
        elif size < 2**30:
            return str(round(size/2**(X*2))) + "МБ"
        elif size < 2**40:
            return str(round(size/2**(X*3))) + "ГБ"


def check_size(size):
    if size >= 0:
        return 0
    else:
        print("Неправильный ввод!")
        return -1
