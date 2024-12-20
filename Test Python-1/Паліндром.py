num = input("Введіть п'ятизначне число: ")

a = int(num[0])
b = int(num[1])
c = int(num[2])
x = int(num[3])
y = int(num[4])

if a == y and b == x :
    print("Паліндром")
else:
    print("Не паліндром")