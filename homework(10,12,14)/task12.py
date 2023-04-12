print("Введите сумму чисел: ")
sum = int(input())
print("Введите произведение чисел: ")
productOfNumbers = int(input())
isFound = False
for number1 in range(productOfNumbers):
    for number2 in range(productOfNumbers):
        if number1 * number2 == productOfNumbers and number1 + number2 == sum:
            if not isFound:
                print(number1)
                print(number2)
                isFound = True
