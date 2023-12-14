acro = []
while True:
    s = input(str("Введите слово: "))
    if s != " ":
        sym = s[0]
        acro += sym 
    else:
        print("Акростих:",''.join(str(el) for el in acro))
        break
