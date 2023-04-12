import random

number_of_coins = int(input("Введите количество монет: "))
heads = 0
tails = 0

for i in range(number_of_coins):
    if random.random() < 0.5:
        heads += 1
        print("Орёл")
    else:
        tails += 1
        print("Решка")

if heads > tails:
    print("Нужно перевернуть " + str(tails) + " монет(ы)")
else:
    print("Нужно перевернуть " + str(heads) + " монет(ы)")
