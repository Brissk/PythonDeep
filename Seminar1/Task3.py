# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна подсказывать «больше» или
# «меньше» после каждой попытки. Для генерации случайного числа используйте код: from random import randint num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint
num = randint(0, 1000)

#Число загадывает компьютер
guess_num = 0
count = 1
while guess_num != num:
    if count > 10:
        print("К сожалению попытки закончились, вы проиграли")
        break
    print("Попытка № ", count)
    guess_num = int(input("Введите предполагаемое число: "))
    if guess_num > num:
        print("Введите число поменьше")
    elif guess_num == num:
        print("Вы угадали! Поздравляю!")
    else:
        print("Введите число побольше")
    count += 1
