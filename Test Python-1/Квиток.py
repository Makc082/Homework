num = input("Введіть шість цифр білету: ")
a = int(num[0])
b = int(num[1])
c = int(num[2])
x = int(num[3])
y = int(num[4])
z = int(num[5])

if a + b + c == x + y + z:
    print("Щасливий квиток")
else:
    print("Не щасливий квиток")