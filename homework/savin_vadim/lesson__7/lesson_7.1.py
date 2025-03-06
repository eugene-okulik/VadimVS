def chance(num):
    while True:
        int_person = int(input("Enter integer: "))
        if num == int_person:
            print("вы угадали")
            break
        else:
            print("вы не угадали")


chance(2)
