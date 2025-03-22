first = int(input("Введите первое число:"))
second = int(input("Введите второе число:"))
operation = ""


def startt(func):
    def wrap(first, second, operation):
        if first < 0 or second < 0:
            operation = "*"
        elif first == second:
            operation = "+"
        elif first > second:
            operation = "-"
        elif first < second:
            operation = "/"
        return func(first, second, operation)
    return wrap


@startt
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second
    return "ввел какую то дичь"


result = calc(first, second, operation)

print(result)
