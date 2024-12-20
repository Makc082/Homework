x = float(input("Введіть масу в тоннах (дробове число): "))
t = int(x)
t1 = x - t
kg = int(t1 * 1000)
gr = int((t1 * 1000 - kg) * 1000)  
print("Тонн - " , t)
print("Кг - " , kg)
print("Гр - " , gr)