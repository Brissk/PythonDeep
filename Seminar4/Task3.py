"""Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег
Дополнительно сохраняйте все операции поступления и снятия средств в список."""

deposit = 0
count = 1
logs = []
def account_add():
    global deposit
    global count
    while True:
        cash = int(input('Введите сумму для пополнения, кратную 50: '))
        if cash % 50 != 0:
            print('Ошибка'+'\n')
        else:
            logs.append("+" + str(cash))
            if count == 3:
                deposit += cash + (cash * 0.03)
                count = 0
                if deposit >= 5000000:
                    deposit *= 0.9
            else:
                deposit += cash
                if deposit >= 5000000:
                    deposit *= 0.9
                count += 1

            break

def account_take():
    global deposit
    global count
    while True:
        cash = int(input('Введите сумму для снятия, кратную 50(комиссия 1,5%): '))
        if deposit > cash:
            if cash % 50 != 0:
                print('Ошибка'+'\n')
            else:
                logs.append("-" + str(cash))
                if count == 3:
                    if cash * 0.015 < 30:
                        deposit -= (cash + 30) + (cash * 0.03)
                        count = 0
                    elif cash * 0.015 > 600:
                        deposit -= (cash + 600) + (cash * 0.03)
                        count = 0
                    else:
                        deposit -= (cash + (cash * 0.015)) + (cash * 0.03)
                        count = 0
                else:
                    if cash * 0.015 < 30:
                        deposit -= (cash + 30)
                        count += 1
                    elif cash * 0.015 > 600:
                        deposit -= (cash + 600)
                        count += 1
                    else:
                        deposit -= (cash + (cash * 0.015))
                        count += 1
                break
        else:
            print('Недостсточно средств')

def account_exit():
    exit()

def deposit_status():
    print(f'На счету: {deposit} руб')

def menu():
    while True:
        action = input('Какое действие вы хотите совершить:\n 1-Пополнить счёт\n 2-Снять со счёта\n 3-Проверить баланс \n 4-Проверить список операций \n 5-Выйти\n')
        match action:
            case '1':
                account_add()
                deposit_status()
            case '2':
                account_take()
                deposit_status()
            case '3':
                deposit_status()
            case '4':
                print(logs)
            case '5':
                account_exit()

menu()