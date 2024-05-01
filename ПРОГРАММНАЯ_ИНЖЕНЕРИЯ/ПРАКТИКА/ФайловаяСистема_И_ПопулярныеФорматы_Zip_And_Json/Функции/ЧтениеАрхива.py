import zipfile
import os

import collections


# def read_zipfile(archive, path=""):
#     os.chdir("../" + path)
#
#     rank = 0
#
#     with zipfile.ZipFile(archive, 'r') as myzip:
#         file_list = []
#         for filename in myzip.namelist():
#             try:
#                 file = filename.encode('cp437').decode('cp866')
#                 for i in range(0, int(len(str(file)))):
#                     try:
#                         if file[i] == "/" and file[i+1] != "":
#                             rank += 1
#                             index_r = i
#                     except IndexError:
#                         break
#                 if rank == 0:
#                     file_list.append([file, rank])
#                     rank = 0
#                 elif rank >= 1:
#                     file_list.append([file[index_r:-1] + file[-1], rank])
#                     rank = 0
#
#             except UnicodeDecodeError:
#                 print('Что то пошло не так...')
#             # Сортируем сначала по глубине (количество '/'), потом по имени
#             sorted_file_list = sorted(file_list, key=lambda x: (x[1], x[0]))
#         return sorted_file_list


# archive1 = "Архив2.zip"
# files_in_arch = read_zipfile(archive1, "Тестирование/Файлы_и_Архивы")
# print(files_in_arch)


def build_file_tree(file_list):
    """
    Строит дерево файлов из списка имен файлов
    """
    tree = {}

    for filename in file_list:
        filename = filename.encode('cp437').decode('cp866')
        # Разбиваем имя файла на части по разделителю "/"
        parts = filename.strip('/').split('/')

        # Временное дерево
        current_level = tree

        # Проходим по каждой части и создаем вложенные словари
        for part in parts:
            if part not in current_level:
                # Если последняя часть (файл), создаем как файл, иначе как папку
                current_level[part] = {}
            current_level = current_level[part]

    return tree


def print_tree(tree, indent=0):
    """
    Рекурсивно выводит дерево файлов
    """
    for key, value in tree.items():
        # Печатаем отступ в зависимости от глубины
        print(" " * indent, key, sep="")

        # Если это папка (имеет вложения), рекурсивно вызываем функцию
        if isinstance(value, dict) and value:
            print_tree(value, indent + 2)


def read_zipfile(archive):
    with zipfile.ZipFile(archive, 'r') as myzip:
        file_list = myzip.namelist()

    # Сортируем по глубине (по числу '/') и имени
    sorted_file_list = sorted(file_list, key=lambda x: (x.count('/'), x))

    # Строим дерево файлов
    file_tree = build_file_tree(sorted_file_list)

    return file_tree


# Используем функцию для чтения ZIP-архива
archive_path = "../Тестирование/Файлы_и_Архивы/Архив2.zip"
file_tree = read_zipfile(archive_path)

# Выводим дерево файлов
print_tree(file_tree)


