num = input("Введіть ціле число (не більше 4 розрядів) : ")
a = int(num[0])
b = int(num[1])
c = int(num[2])
d = int(num[3])

if num == a + b + c + d:
    print("Це чотиризначне число.")
elif num == a + b + c:
    print("Це тризначне число.")
elif num == a + b:
    print("Це двозначне число.")
elif num == a:
    print("Це однозначне число.")
else:
    print("Помилка ! Спробуйте ще !")    