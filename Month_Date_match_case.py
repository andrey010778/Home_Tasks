while True:
    month = int(input("Input month of birth: "))
    if 1<=month<=12:
        break    
    else:
        print("Wrong month. Try it again.")

while True:
    day = int(input("Input your day of birth: "))
    match month:
        case 1|3|5|7|8|10|12:
            if 1<=day<=31:
                print("Month:", month, "Day:", day)
                break    
            else:
                print("Wrong day. Try it again.")
        case 4|6|9|11:
            if 1<=day<=30:
                print("Month:", month, "Day:", day)
                break    
            else:
                print("Wrong day. Try it again.")
        case 2:
            if 1<=day<=29:
                print("Month:", month, "Day:", day)
                break    
            else:
                print("Wrong day. Try it again.")
