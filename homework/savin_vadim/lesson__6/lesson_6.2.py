my_list = list(range(1, 101))
list_result = []
for number in my_list:
    if number % 15 == 0:
        number = "FuzzBuzz"
        list_result.append(number)     
    elif number % 3 == 0:
        number = "Fuzz"
        list_result.append(number)
    elif number % 5 == 0:
        number = "Buzz"
        list_result.append(number)
    else:
        list_result.append(number)
print(list_result)
