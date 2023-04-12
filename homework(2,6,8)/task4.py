totalNumber = float(input("Введите общее количество журавликов: "))
if totalNumber % 2 != 0:
    print("Данное количество не соответствует условию задачи")
else:
    katya = totalNumber / 1.5
    petya = katya / 4
    sergey = katya / 4
    print(f"Катя: {katya}. Петя: {petya}. Сережа: {sergey}")
