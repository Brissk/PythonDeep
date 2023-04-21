"""Добавьте в модуль с загадками функцию, которая хранит словарь списков.
Ключ словаря - загадка, значение - список с отгадками. Функция в цикле
вызывает загадывающую функцию, чтобы передать ей все свои загадки."""
import random


def puzzle(puzzle_text: str, solutions: list[str], tries: int) -> int:
    print(puzzle_text)
    solutions = list(map(lambda x: x.lower(), solutions))
    num = 0
    while num < tries:
        user_input = input('Введите вариант ответа: ').lower()
        if user_input in solutions:
            return num + 1
        else:
            print('Не угадал, попробуй еще')
        num += 1
    return 0


def puzzle_solut():
    dict_puzzle = {'Зимой и летом одним цветом': ['ель', 'елка', 'доллар'],'Висит груша - нельзя скушать': ['груша', 'игрушка', 'лампочка']}

    for key,value in dict_puzzle.items():
        puzzle(key,value,random.randint(3,6))





