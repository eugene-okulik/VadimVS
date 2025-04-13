import argparse
import os


parser = argparse.ArgumentParser(description='Чтение логов')
parser.add_argument('path', help='Полный путь к файлу')
parser.add_argument('--search', required=True, help='Ключевое(ые) слово(а) для поиска')

args = parser.parse_args()

if os.path.isdir(args.path):
    file_paths = [os.path.join(args.path, filename) for filename in os.listdir(args.path)
                  if os.path.isfile(os.path.join(args.path, filename))]
elif os.path.isfile(args.path):
    print("Указан файл, а не папка!")
    exit(1)
else:
    print("Это ни файл, ни папка!")
    exit(1)
for filename in file_paths:
    file_path = os.path.join(args.path, filename)
    try:
        with open(file_path) as open_file:
            for i, row in enumerate(open_file, start=1):
                line = row.strip().split()
                if args.search in line:
                    try:
                        position = line.index(args.search)
                        match position:
                            case _ if position > 4 and position + 5 > len(line):  # Если ключевое слово в конце строки
                                result = " ".join(line[position - 5:])
                                print(f'Найдено в файле: {file_path}',
                                      f'Найдено на строке: {i}, Содержимое строки: {result}')
                            case _ if position > 4 and position + 5 <= len(line):  # Берем данные с одной строки
                                result = " ".join(line[position - 5: position + 5])
                                print(f'Найдено в файле: {file_path}',
                                      f'Найдено на строке: {i}, Содержимое строки: {result}')
                            case _ if position <= 4:  # Если ключевое слово в начала строки
                                result = " ".join(line[0: position + 5])
                                print(f'Найдено в файле: {file_path}',
                                      f'Найдено на строке: {i}, Содержимое строки: {result}')
                    except Exception as e:
                        print(f'Непредвиденная ошибка {e}')
    except Exception as e:
        print(f'Не удалось открыть файл {filename} из за ошибки: {e}')
