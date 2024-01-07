'''109'''

print("1) Create a new file")
print("2) Display the file")
print("3) Add a new item to the file")
selection = int(input("Make a selection 1, 2, or 3:"))
if selection == 1:
    subject = input("Enter a school subject: ")
    file = open("Subject.txt", "w")
    file.write(subject + "\n")
    file.close()
elif selection == 2:
    file = open("Subject.txt", "r")
    print(file.read())
elif selection == 3:
    file = open("Subject.txt", "a")
    subject = input("Enter a school subject: ")
    file.write(subject + "\n")
    file.close()
    file = open("Subject.txt", "r")
    print(file.read())
else:
    print("Invalid option")



'''105-108

file = open("Names.txt", "w")
file.write("Bob\n")
file.write("Tom\n")
file.write("Gemma\n")
file.write("Sarah\n")
file.write("Timothy\n")
file.close()
file = open("Names.txt", "r")
print(file.read())
file.close()
file = open("Names.txt", "a")
newname = input("Enter a new name: ")
file.write(newname + "\n")
file.close()

file = open("Names.txt", "r")
print(file.read())
file.close()'''

''' Комменды при создании чтении и закрытии файла
file = open("Countries.txt", "w")
file.write("Italy\n")
file.write("Germany\n")
file.write("Spain\n")
file.close()
file = open("Countries.txt", "r")
print(file.read())
file = open("Countries.txt", "a")
file.write("France\n")
file.close()'''



'''103-104


list = {}
for i in range(0, 4):
    name = input("Enter namer: ")
    age = int(input("Enter age: "))
    shoe = int(input("Shoe size: "))
    list[name] = {"Age": age, "Shoe size": shoe}

getrid = input("Who do you want to remove from the list?")
del list[getrid]
for name in list:
    print((name), list[name]["Age"], list[name]["Shoe size"]) '''

'''100-101

sales = {"John": {"N": 3056, "S": 8463, "E": 8441, "W":2694},
"Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
"Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
"Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}}
person = input("Enter sales person's name: ")
region = input("Select region: ")
print(sales[person][region])
newdata = int(input("Enter a new data: "))
sales[person][region] = newdata
print(sales[person])'''






'''096 - 099

list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
row = int(input("Select a row: "))
print(list[row])
col = int(input("Select a column: "))
print(list[row][col])
change = input("Do you want to cahnge the value? y/n?")
if change == "y":
    newvalue = int(input("Enter new value: "))
    list[row][col] = newvalue
print(list[row])'''

'''087 Прикольная задача на вывод из списка в обратном порядке

word = input("Enter a word: ")
length = len(word)
num = 1
for x in word:
    position = length - num
    letter = word[position]
    print(letter)
    num = num + 1'''

''''086 Допиленная программа проверки ввода пароля!!! 
while True:
    pswd1 = input('Enter a password: ')
    pswd2 = input('Enter a password: ')
    if pswd1 == pswd2:
        print("Thank you")
        break
    elif pswd1.lower() == pswd2.lower():
        print("They must be in the same case")
    else:
        print("Incorrect")'''

'''079 Странная задача - нужно разобраться с удалением по значению и индексу из списка

nums = []
for i in range(0,3):
    num = int(input("Enter digit"))
    nums.append(num)
print(nums)
question = input("Do you want to save last number?")
if question == "no":
    nums.remove(num)
print(nums) '''

'''077

name1 = input("Input name of person1: ")
name2 = input("Input name of person2: ")
name3 = input("Input name of person3: ")
lst = [name1, name2, name3]
question = input("Do you want to invite somebody else?: (y/n)?")
while question == "y":
    name_add = lst.append(input("Input name of person?"))
    question = input("Do you want to invite somebody else?: (y/n)?")

print("you invited", len(lst), "person")
print(lst)
selection = input("Enter one of the names: ")
print(selection, "is on position", lst.index(selection), "on the list")
stillcome = input("Do you still want them to come? y/n")
if stillcome == "n":
    lst.remove(selection)
print(lst)'''


'''073

food_dictionary = {}
food1 = input("Enter a food you like?: ")
food_dictionary[1] = food1
food2 = input("Enter a food you like?: ")
food_dictionary[2] = food2
food3 = input("Enter a food you like?: ")
food_dictionary[3] = food3
food4 = input("Enter a food you like?: ")
food_dictionary[4] = food4
print(food_dictionary)
dislike = int(input("Which of these food do you want to get rid of? "))
del food_dictionary[dislike]
print(sorted(food_dictionary.values()))'''



'''072
subject_list = ["maths", "english", "computng", "history", "science", "spanish"]
print(subject_list)
dislike = input("Which of these subj do you dislike? ")
getrid = subject_list.index(dislike)
del subject_list[getrid]
print(subject_list)'''



''' 058
import random
score = 0
for i in range(1,6):
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    correct = num1 + num2
    print(num1, "+", num2, "=")
    answer = int(input("Your answer: "))
    print()
    if answer == correct:
        score = score + 1
print(f'"You scored ", {score}, "out of 5"')'''

'''057
import random
num = random.randint(1,10)
count = 0
correct = False
while correct == False:
    guess = int(input("Enter a number: "))
    if guess == num:
        correct = True
    elif guess > num:
        print("Too high")
    else:
        print("Too low")
    count = count + 1

print(f'"Random number was {num}. Your try to attempt: {count} "') '''





'''049
from random import randint
compnum  = int(randint(1, 100))
num = int(input('Please input number 1:100:'))
count = 1
while num != compnum:
     if num > compnum:
         print("Too high")
     elif num < compnum:
         print("Too low")
     count = count + 1
     num = int(input('Print another number'))
print(f'"Correct you try to attempt - {count}"') '''

'''048
again = "y"
count = 0
while again == "y":
    name = input("Enter a name of somebody you want to invite to the party: ")
    print (name, "Has been invited")
    count = count + 1
    again = input ("Do you want to invite somebody else? y/n")
print("You have", count, "people coming to your party") '''

''' Task 044
    numb_of_p = int(input("How many people do you want to invite? :"))
if numb_of_p < 10:
    for i in range(0, numb_of_p):
        names = input('Names of in inviting people:')
        print(names, 'has been inviting')
else:
    print("Too many people") '''

'''Задача на вычисление площади и создание меню функции'''

#print("1) Square")
#print("2) Triangle")
#print()
#menuselection = int(input("Enter a number: "))
# if menuselection == 1:
#    side = int(input("Enter the length of one side: "))
#    area = side * side
#    print ("The area of your chosen shape is ", area)
#elif menuselection == 2:
#    base = int(input(Enter the length ))
