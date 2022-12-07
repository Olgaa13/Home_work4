# 1'. Вычислить число Пи c заданной точностью d
# *Пример:* 
# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415  
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from math import pi
d = float(input("Задайте значение точности для π: "))
def calc_fract(number_count):
    count = 0
    while number_count % 1 != 0:
        number_count *= 10
        count += 1
    return count
if d == 10**(-1) or d == 10**(-2) or d == 10**(-3)\
or d == 10**(-4) or d == 10**(-5) or d == 10**(-6)\
or d == 10**(-7) or d == 10**(-8) or d == 10**(-9)\
or d == 10**(-10): 
    new_d = calc_fract(d)
    print(f'число π с заданной точностью {d} = {round(pi, new_d)}')
else:
    print('Число не соответствует условию:')
    



# Решение от преподавателя:

from math import pi    


def format_by_mask(num: float, accuracy: float) -> float:
    """"форматирует число по заданной маске"""
    accuracy = str(accuracy)
    accuracy = len(accuracy[accuracy.find('.')+1::])
    return float(f'{pi:0.{accuracy}f}')    # f'a:0.3f'


d = input('Введите точность в формате "0.001": ')
print(format_by_mask(pi, d))
