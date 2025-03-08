import random


def salary_bonus():
    salary = int(input("Введи сумму: "))
    bonus = random.choice([True, False])
    if bonus is True:
        salary_new = salary + random.randint(500, 3000)
    else:
        salary_new = salary
    print(f"{salary}, {bonus} - '${salary_new}'")


salary_bonus()
