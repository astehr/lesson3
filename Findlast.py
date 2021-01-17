import os

path = r'C:\Users\fedia\PycharmProjects\Lesson3\File'

x = []

for file in os.listdir(path):
    if file.endswith('.txt'):
        x.append(os.path.join(path, file))

a = max(x, key=os.path.getctime)


full_file = [] #список с нужными строками

j = open(a, 'r')
for y in j.readlines():
    full_file.append(y)
j.close()
"""Я не нашел способа проще, чем взять и закинуть содержимое файла в список, чтобы потом его отредактировать в мейне 
и переложить в новый файл"""

