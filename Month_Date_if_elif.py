while True:
    month = int(input("Input month of birth: "))
    if 1<=month<=12:
        break    
    else:
        print("Wrong month. Try it again.")

while True:
    day = int(input("Input your day of birth: "))
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if 1<=day<=31:
            print("Month:", month, "Day:", day)
            break    
        else:
            print("Wrong day. Try it again.")
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if 1<=day<=30:
            print("Month:", month, "Day:", day)
            break    
        else:
            print("Wrong day. Try it again.")
    elif month == 2:
        if 1<=day<=29:
            print("Month:", month, "Day:", day)
            break    
        else:
            print("Wrong day. Try it again.")
