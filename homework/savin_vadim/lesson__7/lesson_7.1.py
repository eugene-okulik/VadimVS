def chance():
    num = 11
    while True:
        int_person = int(input("Введите число: "))
        if num == int_person:
            print("Поздравляю! Вы угадали!")
            break
        else:
            print("попробуйте снова")


chance()
