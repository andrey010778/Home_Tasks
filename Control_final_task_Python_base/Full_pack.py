from Logic import add_record, show_all, show_for_date, show_by_category, show_by_min_max, delete_row

def main():
    tryagain = True
    while tryagain == True:
        print("Hello", "\n")
        print("1. Add")
        print("2. Show all")
        print("3. Show for date")
        print("4. Show by category")
        print("5. Show by min->max")
        print("6. Delete")
        print("0. Exit")
        print()
        menuselection = int(input("What would you like to do?: "))
        if menuselection == 1:
            add_record()
        elif menuselection == 2:
            show_all()
        elif menuselection == 3:
            show_for_date()
        elif menuselection == 4:
            show_by_category()
        elif menuselection == 5:
            show_by_min_max()
        elif menuselection == 6:
            delete_row()
        elif menuselection == 0:
            print("Thank you")
            tryagain = False
        else:
            print("try again") # красиво возвращаемся к while True тк нет break'''


main()