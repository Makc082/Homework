a = int(input("Введіть перше ціле значення: "))
b = int(input("Введіть друге ціле значення: "))
c = int(input("Введіть третє ціле значення: "))

if a < b and a < c:
    print(a)
elif b < a and b < c:
    print(b)
elif c < a and c < b:
    print(c) 