import argparse


parser = argparse.ArgumentParser(description='Чтение логов')
parser.add_argument('path', help='Полный путь к файлу')
parser.add_argument('--search', required=True, help='Ключевое(ые) слово(а) для поиска')


args = parser.parse_args()

with open(args.path) as open_file:
    previous_row = None

    for i, row in enumerate(open_file, start=1):
        line = row.strip().split()
        if args.search in line:
            try:
                position = line.index(args.search)
                if position > 4 and position + 5 > len(line):
                    future_row = next(open_file, None)
                    if future_row is not None:
                        future_index = abs(len(line) - (position + 5))
                        result = " ".join(line[position - 5:] + (future_row.strip()).split()[:future_index])
                        print(f'Найдено в файле: {args.path}',
                              f'Найдено на строке: {i}, Содержимое строки: {result}')
                    else:
                        result = " ".join(line[position - 5:])
                        print(f'Найдено в файле: {args.path}',
                              f'Найдено на строке: {i}, Содержимое строки: {result}')
                elif position > 4 and position + 5 <= len(line):
                    result = " ".join(line[position - 5: position + 5])
                    print(f'Найдено в файле: {args.path}',
                          f'Найдено на строке: {i}, Содержимое строки: {result}')
                elif position <= 4 and i < 2:
                    result = " ".join(line[0: position + 5])
                    print(f'Найдено в файле: {args.path}',
                          f'Найдено на строке: {i}, Содержимое строки: {result}')
                elif position <= 4 and i > 1:
                    start_position = position - 5
                    result = " ".join(previous_row[start_position:] + line[0: position + 5])
                    print(f'Найдено в файле: {args.path}',
                          f'Найдено на строке: {i}, Содержимое строки: {result}')
            except Exception as e:
                print(f'Непредвиденная ошибка {e}')
            previous_row = line
