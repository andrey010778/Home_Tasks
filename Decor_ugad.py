from random import randint

n_comp = randint(1, 100)
print('Компьютер "загадал" число в интервале от 1 до 100. Какое?')


def counter(func):
    def wrapper(*args):
        wrapper.count += 1
        return func(*args)

    wrapper.count = 0
    return wrapper


@counter
def check_numder(numder, n_comp):
    if numder > n_comp:
        return 'Загаданное число меньше'
    elif otvet < n_comp:
        return 'Загаданное число больше.'
    else:
        return otvet


while True:
    otvet = int(input('Введите Ваше число '))
    answer = check_numder(otvet, n_comp)
    print(answer)
    if otvet == n_comp:
        break

print('Правильно! Число попыток отгадывания:', check_numder.count)