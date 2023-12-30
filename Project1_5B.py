''' Функция для вычисления среднего списка значений температуры'''
def average_of_temp():
    days_of_list = [1, 2, 10, 25, 'None', 47, 32]
    for i in days_of_list:
        if i == 'None':
            days_of_list.remove('None')
    average = sum(days_of_list) / len(days_of_list)
    return average

print(average_of_temp())


''' Функция для принятия значений и формирования кортежей'''
def pim(*c):
    str_1 = []
    str_2 = []
    for i in c:
        if i > 0:
            str_1.append(float(format(i, '.2f')))
        elif i < 0:
            str_2.append(float(format(i, '.2f')))
    str_1.sort()
    str_2.sort(reverse=True)
    print(list(zip(str_1, str_2)))

pim(1.356, -20, 40, 86, -312)

'''Функция возведения в степень целых чисел'''
def to_n(a, b):
    return (a**b)

a = int(input('Input a: '))
b = int(input('Input stepen: '))
print(to_n(a,b))

'''Функция возведения в степень с рекурсией'''
def to_recurse(a,b):
    if b == 1:
        return(a)
    if b !=1:
        return (a * to_recurse(a, b - 1))

a = int(input('Input a: '))
b = int(input('Input stepen: '))
print(to_recurse(a,b))


