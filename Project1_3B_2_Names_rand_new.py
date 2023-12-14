import names, random, numpy as np

rows = 100
id = np.array(range(1,100))
firstname = np.array([''.join(names.get_first_name()) for _ in range(rows)])
b = []
c = []
for i in firstname:
    if "A" <= i[0] <= "M":
        b += [i]
    else:
        c += [i]
print(b)
print(c)
