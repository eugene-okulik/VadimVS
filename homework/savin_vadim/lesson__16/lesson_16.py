import dotenv
import os
import csv
import mysql.connector as my_sql

dotenv.load_dotenv()


this_dir = os.path.dirname(__file__)
path_csv = os.path.join(os.path.dirname(os.path.dirname(this_dir)),
                        'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')


def read_file():
    with open(path_csv, newline='') as csv_file:
        file_data = csv.reader(csv_file)
        data = [row for row in file_data]
        return data[1:]


def new_cursor(db):
    return db.cursor(dictionary=True)


def parse_data(db, data_list):  # распаковываем для SQL запроса
    not_found = []
    for name, second_name, group_title, book_title, subject_title, lesson_title, mark_value in data_list:
        with new_cursor(db) as cursor:
            select_data = '''Select * from students s
                            LEFT JOIN books b ON s.id = b.taken_by_student_id
                            LEFT JOIN marks m ON s.id = m.student_id
                            LEFT JOIN lessons l ON m.lesson_id = l.id
                            LEFT JOIN `groups` g ON s.group_id = g.id
                            LEFT JOIN subjets s2 ON s2.id = l.subject_id
                            WHERE s.name = %s AND s.second_name = %s AND g.title = %s
                            AND b.title = %s AND s2.title = %s AND l.title = %s
                            AND m.value = %s
                            '''
            cursor.execute(select_data, ((name, second_name, group_title, book_title,
                                          subject_title, lesson_title, mark_value)))
            result = cursor.fetchall()
            if not result:
                not_found.append((name, second_name, group_title, book_title, subject_title, lesson_title, mark_value))
            else:
                print("Строка найдена: ", result)
    if db.is_connected():
        db.close()
    print(not_found)


db = my_sql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

data_csv = read_file()
parse_data(db, data_csv)
