
def selection():
    print("1. Add")
    print("2. Edit")
    print("3. Exit")
    print()
    while True:
        menuselection = int(input("Enter a point of menu"))
        if menuselection == 1 or menuselection == 2:
            break # нужно действие после выбора каждого меню'''
        elif menuselection == 3:
            print("Thank you")
            break
        else:
            print("try again") # красиво возвращаемся к while True тк нет break'''
    # return selection() - убрать ибо влетаем в цикл

selection()

''' Упёрся в вызов функции'''









