x = int(input("Введіть значення: "))

if x % 3 == 0 and x % 5 == 0 and x % 7 == 0:
    print("Кратне")
else:
    print("Не кратне")