"""Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента.
Если ключ не хешируем, используйте его строковое представление. ."""

my_dict = {}

def key_elem(**kwargs):
    for key, value in kwargs.items():
        my_dict[value] = str(key)
        # print(value,key)
    return my_dict

print(key_elem(name='Mikle', number=5, work='Easy' ))