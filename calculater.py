from min import my_minimum
from min import my_plus
a = int(input('Введите число а: '))

b = int(input('Введите число b: '))


action = input( 'Введите действие. Допустимо: plus, minus, koren, stepen, umnoj, deli, sred, min, max, sumX2  : ')

if action == 'plus':
    result = a + b
    print(result)
elif action == 'minus':
    result = a - b
    print(result)
elif action == 'min':
    result = my_minimum(a,b)
    print(result)


