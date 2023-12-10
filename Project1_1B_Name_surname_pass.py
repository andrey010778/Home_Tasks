
name, surname=input('Name ''Surname').split()
cap_name=name.capitalize()
cap_surname=surname.capitalize()
second_1symb=cap_name[:1]
first_4symb=cap_surname[:4]
login=first_4symb+second_1symb
print(cap_surname, cap_name, ':',login)