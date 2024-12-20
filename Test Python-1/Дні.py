x = int(input("Введіть данні в секундах: "))
day = x // 86400
y = x % 86400
hr = y // 3600
y %= 3600
min = y // 60
sec = y % 60
print("Дні: " , day)
print("Години: " , hr)
print("Хвилини: "  , min)
print("Секунди: " , sec)