import os
import datetime

my_dir = os.path.dirname(__file__)
file_path = (os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                          "eugene_okulik", "hw_13", "data.txt"))
new_file_path = os.path.join(os.path.dirname(__file__), "data_hw_13.txt")


def read_file():
    with open(file_path, "r") as data_file:  # Открываем файл для чтения
        for line in data_file:
            yield line


line = read_file()

for data_line in line:
    with open(new_file_path, 'a') as new_file:
        split_text = data_line.split()
        date = split_text[1] + " " + split_text[2]  # Вытаскиваем "2023-11-27 20:34:13.212967"
        date_parcing = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
        if data_line.startswith("1."):
            data_type_date1 = date_parcing + datetime.timedelta(days=7)
            result_date_line1 = datetime.datetime.strftime(data_type_date1, "%Y-%m-%d %H:%M:%S.%f")
            new_file.write(result_date_line1 + "\n")
        elif data_line.startswith("2."):
            result_date_line2 = datetime.datetime.strftime(date_parcing, "%A")
            new_file.write(result_date_line2 + "\n")

        elif data_line.startswith("3."):
            data_type_date3 = (datetime.datetime.now() - date_parcing).days
            new_file.write(str(data_type_date3))
