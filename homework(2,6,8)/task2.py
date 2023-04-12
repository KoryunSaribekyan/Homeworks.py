number = int(input("Введите трехзначное число: "))
number1 = number // 100
number2 = (number // 10) % 10
number3 = number % 10
sum = number1 + number2 + number3
print("Сумма цифр равна:", sum)
