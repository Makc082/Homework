# a1,b1 - години , a2,b2 - хвилини , x - час розмови , y - вартість , z = вартість розмови.
a = float(input("Початок розмови (години.хвилини): "))
b = float(input("Кінець розмови (години.хвилини): "))

a1 = int(a)
b1 = int(b)

a2 = (a - a1) * 100
b2 = (b - b1) * 100

x = b1 * 60 + b2
x1 = a1 * 60 + a2
y = 0.15
z = (x - x1) * y 

print("Вартість розмови в гривнях: " , z)