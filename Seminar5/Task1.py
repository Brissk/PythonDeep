"""Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла."""



path = 'D:/2-Different/10-Business./Programming/1-VSCode projects/2-GeekBrains/1-html+css+JS/style.css'


def name_file(path):
    return (path.rsplit('/',1)[0], path.split('/')[-1].split('.')[0],path.split('/')[-1].split('.')[1])

print(name_file(path))












