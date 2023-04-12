number = int(input("Введите шестизначное число: "))
sum1 = ((number // 1000) % 10) + ((number // 10000) % 10) + (number // 100000)
sum2 = number % 10 + ((number // 10) % 10) + ((number // 100) % 10)

if sum1 == sum2:
    print("Yes")
else:
    print("No")
