chocolate_length = int(input("Введите длину шоколадки: "))
chocolate_width = int(input("Введите ширину шоколадки: "))
number_of_slices = int(input("Сколько долек нужно отломать: "))

chocolate_size = chocolate_length * chocolate_width
if number_of_slices % chocolate_width == 0 or number_of_slices % chocolate_length == 0:
    print("Yes")
else:
    print("No")
