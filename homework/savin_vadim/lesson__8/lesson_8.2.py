import time


def fibo(iteration):
    first_int, second_int = 0, 1
    count = 0
    while count < iteration:
        result = first_int + second_int
        yield first_int
        first_int = second_int
        second_int = result
        count += 1


def data_fibo_count(iteration):
    count = 1
    for number in fibo(iteration):
        if count == iteration:
            print(f"{iteration}-е число Фибоначчи: {number}")
            break  
        count += 1

data_fibo_count(10)
data_fibo_count(200)
data_fibo_count(1000)
data_fibo_count(100000)