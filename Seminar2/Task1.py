"""Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата. """

num = int(input("Enter a number: "))
x = num
result = ""
while num:
    if num % 16 == 10:
        result += "A"
    elif num % 16 == 11:
        result += "B"
    elif num % 16 == 12:
        result += "C"
    elif num % 16 == 13:
        result += "D"
    elif num % 16 == 14:
        result += "E"
    elif num % 16 == 15:
        result += "F"
    else:
        result += str(num % 16)
    num //= 16
print(result[::-1])
print(hex(x))
