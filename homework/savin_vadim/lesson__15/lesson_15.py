import re
import mysql.connector as mysql


db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl',
)


def new_cursor(db):  # Создание курсора
    return db.cursor(dictionary=True)


def close_connect(db):  # Закрыие соединения с БД
    db.close()


def insert_students(db):  # Добавляем студента
    try:
        cursor = new_cursor(db)
        name = input('Введите name: ')
        second_name = input('Введите second_name: ')
        insert_student_query = "insert into students (name, second_name) VALUES (%s, %s)"
        cursor.execute(insert_student_query, (name, second_name))  # Создаем студента
        student_id = cursor.lastrowid  # Получаем id cтудента и записываем в переменную
        db.commit()
        return student_id
    except Exception as exc:
        db.rollback()
        print(f"Не удалось создать студента из-за ошибки: {exc}")
        return None
    finally:
        cursor.close()


def select_last_create(db, table):  # Получаем id последней созданной записи, своего рода "хелпер"
    if not re.match(r"^(a-zA-Z)+$", table):
        print("Введи нормальное название таблицы")
        return None
    else:
        try:
            cursor = new_cursor(db)
            cursor.execute(f"Select id from {table} "
                           "Order by id DESC "
                           "Limit 1")
            last_id = cursor.fetchone()
            if last_id:
                return last_id[0]
            else:
                return None
        except Exception as exc:
            db.rollback()
            print(f"Не удалось получить ID послеедней записи из-за ошибки: {exc}")
            return None
        finally:
            cursor.close()


def insert_book(db, student_id):  # Добавляем книгу
    try:
        cursor = new_cursor(db)
        title_book = input("Введите название книги: ")
        insert_books_query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
        cursor.execute(insert_books_query, (title_book, student_id))
        book_id = cursor.lastrowid
        db.commit()
        return book_id
    except Exception as exc:
        db.rollback()
        print(f"Не удалось создать книгу из-за ошибки: {exc}")
        return None
    finally:
        cursor.close()


def insert_group(db):  # Добавляем группу
    try:
        cursor = new_cursor(db)
        title = input("Введите название группы: ")
        start_date = input("Введите дату вступления в группу: ")
        end_date = input("Введите дату выхода из группы: ")
        insert_books_query = "insert into `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
        cursor.execute(insert_books_query, (title, start_date, end_date))
        group_id = cursor.lastrowid
        db.commit()
        return group_id
    except Exception as exc:
        db.rollback()
        print(f"Не удалось создать группу из-за ошибки: {exc}")
        return None
    finally:
        cursor.close()


def set_student_in_group(db, group_id, id_student):  # Определяем студента в группу
    try:
        cursor = new_cursor(db)
        set_group_for_student = ("Update students set group_id = %s "
                                 "Where id = %s")
        cursor.execute(set_group_for_student, (group_id, id_student))
        db.commit()
        print(f"Студент с id {id_student} был успешно добавлен в группу с id {group_id}")
    except Exception as exc:
        db.rollback()
        print(f"Не удалось определить студента в группу {group_id} и за ошибки {exc}")
        return None
    finally:
        cursor.close()


def insert_subjets(db):  # Добавляем предмет
    try:
        cursor = new_cursor(db)
        title_subjets = input("Введите название предмета: ")
        insert_subjets_query = "insert into subjets (title) VALUES (%s)"
        cursor.execute(insert_subjets_query, (title_subjets,))
        subjets_id = cursor.lastrowid
        db.commit()
        return subjets_id
    except Exception as exc:
        db.rollback()
        print(f"Не удалось создать предмет из-за ошибки: {exc}")
        return None
    finally:
        cursor.close()


def insert_lesson(db, subject_id):  # Добавляем урок
    try:
        cursor = new_cursor(db)
        title_lesson = input("Введите название урока: ")
        insert_lesson_query = "insert into lessons (title, subject_id) VALUES (%s, %s)"
        cursor.execute(insert_lesson_query, (title_lesson, subject_id))
        lesson_id = cursor.lastrowid
        db.commit()
        return lesson_id
    except Exception as exc:
        db.rollback()
        print(f"Не удалось создать урока из-за ошибки: {exc}")
        return None
    finally:
        cursor.close()


def insert_mark(db, lesson_id, student_id):  # Добавляем оценку
    try:
        cursor = new_cursor(db)
        value = input("Введите оценку: ")
        if not re.match(r"^\d+$", value):
            return "Введена некорректная оценка! Ожидается только цифра."
        insert_mark_query = "insert into marks (value, lesson_id , student_id ) VALUES (%s, %s, %s)"
        cursor.execute(insert_mark_query, (value, lesson_id, student_id))
        mark_id = cursor.lastrowid
        db.commit()
        return mark_id
    except Exception as exc:
        db.rollback()
        print(f"Не удалось создать урока из-за ошибки: {exc}")
        return None
    finally:
        cursor.close()


def select_all_mark(db, student_id):  # Получаем все оценки у студента
    try:
        cursor = new_cursor(db)
        select_mark = ("Select * from marks "
                       "Where student_id = %s")
        cursor.execute(select_mark, (student_id,))
        result = cursor.fetchall()
        print(result)
    finally:
        cursor.close()


def select_taken_book(db, student_id):  # Получаем книги полученные студентом
    try:
        cursor = new_cursor(db)
        select_taken = ("select * from books "
                        "WHERE taken_by_student_id  = %s")
        cursor.execute(select_taken, (student_id,))
        result = cursor.fetchall()
        print(result)
    finally:
        cursor.close()


def all_student_data(db, student_id):  # ПОлучаем все данные, которые есть по студенту в БД
    try:
        cursor = new_cursor(db)
        select_taken = ("SELECT s.id as student_id, s.name, s.second_name, "
                        "g.id as group_id, g.title as group_name, g.start_date, g.end_date, "
                        "GROUP_CONCAT(DISTINCT b.id) as book_id, "
                        "GROUP_CONCAT(DISTINCT b.title) as book_title, "
                        "GROUP_CONCAT(DISTINCT m.id) as mark_id, "
                        "GROUP_CONCAT(DISTINCT m.value) as mark_value, "
                        "GROUP_CONCAT(DISTINCT l.id) as lesson_id, "
                        "GROUP_CONCAT(DISTINCT l.title) as lesson_title, "
                        "GROUP_CONCAT(DISTINCT s2.id) as subject_id, "
                        "GROUP_CONCAT(DISTINCT s2.title) as subject_title "
                        "FROM students s LEFT JOIN `groups` g ON s.group_id = g.id "
                        "LEFT JOIN books b ON s.id = b.taken_by_student_id "
                        "LEFT JOIN marks m ON s.id = m.student_id "
                        "LEFT JOIN lessons l ON m.lesson_id = l.id"
                        " LEFT JOIN subjets s2 ON s2.id = l.subject_id "
                        "WHERE s.id = %s "
                        "GROUP BY s.id, s.name, s.second_name, g.id, g.title, g.start_date, g.end_date")
        cursor.execute(select_taken, (student_id,))
        result = cursor.fetchall()
        print(result)
    finally:
        cursor.close()


def work_flow_db():  # объедиинл, чтобы точно отключиться от БД даже в случае ошибки
    try:
        my_student = insert_students(db)
        insert_book(db, my_student)
        my_group = insert_group(db)
        set_student_in_group(db, my_group, my_student)
        my_subject = insert_subjets(db)
        my_lesson = insert_lesson(db, my_subject)
        insert_mark(db, my_lesson, my_student)

        select_all_mark(db, my_student)
        select_taken_book(db, my_student)
        all_student_data(db, my_student)
    finally:
        close_connect(db)


work_flow_db()
