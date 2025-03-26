class Book:
    pages_of_material = "бумага"
    text_availability = True

    def __init__(self, book_title, author, number_of_pages, ISBN, reserved):
        self.book_title = book_title
        self.author = author
        self.number_of_pages = number_of_pages
        self.ISBN = ISBN
        self.reserved = reserved
        reserved_info = ", зарезервировано" if reserved else ""
        print(f"Название: {self.book_title}, Автор: {self.author}, страниц:"
              f"{self.number_of_pages}, материал: {Book.pages_of_material}{reserved_info}")


class ChildrenBook(Book):
    def __init__(self, book_title, author, number_of_pages, ISBN, lesson, class_for_book, reserved, available_tasks):
        super().__init__(book_title, author, number_of_pages, ISBN, reserved)
        self.lesson = lesson
        self.class_for_book = class_for_book
        self.available_tasks = available_tasks
        reserved_info = ", зарезервировано" if reserved else ""
        print(f"Название: {self.book_title}, Автор: {self.author}, страниц:"
              f"{self.number_of_pages}, предмет: {lesson}, "
              f"класс:{class_for_book}{reserved_info}")


# Parth 1
Book("Идиот", "Достоевский", 500, "ISBN", True)
Book("Преступление и наказание", "Достоевский", 672, "ISBN", False)
Book("Мастер и Маргарита", "Булгаков", 480, "ISBN", True)
Book("Война и мир", "Толстой", 1225, "ISBN", False)
Book("Человек-невидимка", "Герберт Уэллс", 320, "ISBN", True)
# Parth 2
ChildrenBook("Геометрия", "Петров", 180, "ISBN", "Математика", 8, True, 50)
ChildrenBook("Литература", "Смирнова", 250, "ISBN", "Литература", 10, False, 60)
ChildrenBook("Физика", "Сидоров", 300, "ISBN", "Физика", 11, True, 70)
ChildrenBook("Биология", "Кузнецова", 220, "ISBN", "Биология", 7, False, 40)
ChildrenBook("История", "Орлов", 275, "ISBN", "История", 9, True, 80)
