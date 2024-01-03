
def selection():
    print("1. Add")
    print("2. Edit")
    print("3. Exit")
    print()
    while True:
        menuselection = int(input("Enter a point of menu"))
        if menuselection == 1 or menuselection == 2:
            break
        elif menuselection == 3:
            print("Thank you")
            break
        else:
            print("try again")
    return selection()

selection()

''' Упёрся в вызов функции'''









