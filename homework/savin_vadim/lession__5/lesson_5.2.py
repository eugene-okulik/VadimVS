# Задание 2
result_one = "результат операции: 42"
result_two = "результат операции: 514"
result_programm = "результат работы программы: 9"

# Можно сделать по действиям, 
# но попытался поломать голвоу над однострочным решением
print(int((result_one[(result_one.index(":"))+1:]).lstrip())+10)
print(int((result_two[(result_two.index(":"))+1:]).lstrip())+10)
print(int((result_programm[(result_programm.index(":"))+1:]).lstrip())+10)
