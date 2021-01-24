import os

PATH_TO_DIR = '/File'

x = []

for file in os.listdir(PATH_TO_DIR):
    if file.endswith('.txt'):
        x.append(os.path.join(PATH_TO_DIR, file))

a = max(x, key=os.path.getctime)


full_file = [] #список с нужными строками

j = open(a, 'r')
for y in j.readlines():
    full_file.append(y)
j.close()
"""Я не нашел способа проще, чем взять и закинуть содержимое файла в список, чтобы потом его отредактировать в мейне 
и переложить в новый файл"""

