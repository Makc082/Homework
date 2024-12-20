print("Виберіть тварину:")
print("Кіт")
print("Собака")
print("Корова")
print("Коза")
print("Вівця")
print("Ворон")

choice = input("Оберіть тварину: ")

match choice:
    case "Кіт":
        print("Мяу")
    case "Собака":
        print("Гав ")
    case "Корова":
        print("Му")
    case "Коза":
            print("Мє")
    case "Вівця":
            print("Бє")
    case "Ворон":
        print("Кар")
    case _:
          print("Оберіть іншу тварину")