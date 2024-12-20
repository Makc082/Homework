num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))

print("Виберіть дію:")
print("+")
print("-")
print("*")
print("/")
print("%")

choice = input("Введіть символ дії: ")

match choice:
    case "+":
        result = num1 + num2
        print("Результат додавання: " , result)
    case "-":
        result = num1 - num2
        print("Результат віднімання: " , result)
    case "*":
        result = num1 * num2
        print("Результат множення: " , result)
    case "/":
        if num2 == 0:
            print("Ділення на 0 неможливе!")
        else:
            result = num1 / num2
            print("Результат ділення: " , result)
    case "%":
        if num2 == 0:
            print("Ділення на 0 неможливе!")
        else:
            result = num1 % num2
            print("Залишок від ділення: " , result)
    case _:
        print("Невірний вибір операції!")