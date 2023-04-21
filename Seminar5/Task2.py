"""Напишите однострочный генератор словаря, который принимает
на вход три списка одинаковой длины: имена str, ставка int,
премия str с указанием процентов вида «10.25%». В результате
получаем словарь с именем в качестве ключа и суммой
премии в качестве значения. Сумма рассчитывается
как ставка умноженная на процент премии"""
from pprint import pprint

name = ['Mikle','Ivan','Kate']
bet = [50000,40000,30000]
bonus = ['10.25%','9.15%','6.7%']


my_gen = {key : value + (value*(float(k.replace('%',''))/100 )) for (key,value,k) in zip(name,bet,bonus) }
pprint(my_gen)


