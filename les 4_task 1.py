from sys import argv

_, hour, stavka, bonus, *__ = argv

try:
    salary = float(hour)*float(stavka)+float(bonus)
    print(f'Ваша заработная плата составляет {salary}')
except ValueError as e:
    print('Ошибка')
    print(e)