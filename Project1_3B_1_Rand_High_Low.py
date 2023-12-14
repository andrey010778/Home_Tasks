from random import randint
lst = [randint(1, 100) for i in range(20)]
lst1 = []
for i in lst:
    if i >= 69:
        n = ["High"]
    else:
        n = ["Low"]
    lst1 += n
print(lst1)
