




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
