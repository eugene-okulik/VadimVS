# Задание 3
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
students_one, students_two, students_tree = students
subjects_one, subjects_two, subjects_tree = subjects

# example f-string
print(f"Students {students_one}, {students_two}, {students_tree} "
      f"study these subjects: {subjects_one}, {subjects_two}, {subjects_tree}")

# example string format
students_msg = ", ".join(students)
subjects_msg = ", ".join(subjects)
my_text = "Students {0} study these subjects: {1}"
print(my_text.format(students_msg, subjects_msg))