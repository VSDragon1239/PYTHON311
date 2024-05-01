import os
from ПреобразовываниеЧЧФ import human_read_format as hrform


# Чтение всех файлов в папке, с флажком только чтение файлов (не надо читать папки)
def get_files_sizes(path="", only_read_files=True):
    list_files = []
    list_files_and_folders = []
    list_all = []

    for file in os.listdir(os.chdir("../" + path)):
        file_and_size = {os.path.splitext(file): hrform(os.path.getsize(file))}
        if os.path.isfile(file):
            list_files.append(file_and_size)
            list_files_and_folders.append(file_and_size)
        else:
            list_files_and_folders.append(file_and_size)

    if only_read_files:
        for file_name in list_files:
            for i in file_name.values():
                for x in file_name.keys():
                    list_all.append([x[0], x[1], i])
        return list_all
    else:
        for file_name in list_files_and_folders:
            for i in file_name.values():
                for x in file_name.keys():
                    list_all.append([x[0], x[1], i])
        return list_all


