"""Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions. """

import fractions

# str1 = input("Enter fraction1: ")
# str2 = input("Enter fraction2: ")
str1 = "1/3"
str2 = "3/5"

a = ""
b = ""
for i in range(len(str1)):
    if str1[i].isdigit():
        a += str1[i]
    else:
        a += " "
for i in range(len(str2)):
    if str2[i].isdigit():
        b += str2[i]
    else:
        b += " "
result = a + " " + b
res = result.split()
# sum = res[0]*res[3]+res[2]*res[1]
print(f'Сумма дробей: {int(res[0])*int(res[3])+int(res[2])*int(res[1])}/{int(res[1])*int(res[3])}')
print(f'Произведение дробей: {int(res[0])*int(res[2])}/{int(res[1])*int(res[3])}')

f1 = fractions.Fraction(1,3)
f2 = fractions.Fraction(3,5)
print(f1+f2)
print(f1*f2)
