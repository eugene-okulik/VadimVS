class Book:
    pages_of_material = "бумага"
    text_availability = True

    def __init__(self, book_title, author, number_of_pages, ISBN, reserved=False):
        self.book_title = book_title
        self.author = author
        self.number_of_pages = number_of_pages
        self.ISBN = ISBN
        self.reserved = reserved

    def result(self):
        reserved_info = ", зарезервировано" if self.reserved else ""
        print(f"Название: {self.book_title}, Автор: {self.author}, страниц: "
              f"{self.number_of_pages}, материал: {Book.pages_of_material}{reserved_info}")


class ChildrenBook(Book):
    def __init__(self, book_title, author, number_of_pages, ISBN, reserved, lesson, class_for_book, available_tasks):
        super().__init__(book_title, author, number_of_pages, ISBN, reserved)
        self.lesson = lesson
        self.class_for_book = class_for_book
        self.available_tasks = available_tasks

    def result(self):
        reserved_info = ", зарезервировано" if self.reserved else ""
        print(f"Название: {self.book_title}, Автор: {self.author}, страниц: "
              f"{self.number_of_pages}, предмет: {self.lesson}, "
              f"класс: {self.class_for_book}{reserved_info}")


# Book
b1 = Book("Идиот", "Достоевский", 500, "ISBN", True)
b2 = Book("Преступление и наказание", "Достоевский", 672, "ISBN", False)
b3 = Book("Мастер и Маргарита", "Булгаков", 480, "ISBN", True)
b4 = Book("Война и мир", "Толстой", 1225, "ISBN", False)
b5 = Book("Человек-невидимка", "Герберт Уэллс", 320, "ISBN", False)
# ChildrenBook
cb1 = ChildrenBook("Геометрия", "Петров", 180, "ISBN", True, "Математика", 8, 50)
cb2 = ChildrenBook("Литература", "Смирнова", 250, "ISBN", False, "Литература", 10, 60)
cb3 = ChildrenBook("Физика", "Сидоров", 300, "ISBN", True, "Физика", 11, 70)
cb4 = ChildrenBook("Биология", "Кузнецова", 220, "ISBN", False, "Биология", 7, 40)
cb5 = ChildrenBook("История", "Орлов", 275, "ISBN", True, "История", 9, 80)

# Book result
b1.result()
b2.result()
b3.result()
b4.result()
b5.result()
# ChildrenBook result
cb1.result()
cb2.result()
cb3.result()
cb4.result()
cb5.result()
