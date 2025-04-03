insert into students (id, name, second_name, group_id) VALUES (53 ,'Rulon', 'Oboev', 2)
insert into books (title, taken_by_student_id) VALUES ('The Hitchhikers Guide to the Galaxy', 53)
insert into books (title, taken_by_student_id) VALUES ('Harry Potter', 53)
insert into books (title, taken_by_student_id) VALUES ('Mémoires de la vie privée de Benjamin Franklin', 53)

insert into `groups` (id, title, start_date, end_date) VALUES (2, 'activist', 'mar 2025', 'may 2025')

insert into subjets (title) VALUES ('Savin AQA')
insert into subjets (title) VALUES ('Savin SQL')
insert into subjets (title) VALUES ('Savin Python')


insert into lessons  (title, subject_id) VALUES ('SQL_svs', 10044)
insert into lessons  (title, subject_id) VALUES ('AQA_svs', 10043)
insert into lessons  (title, subject_id) VALUES ('Python_svs', 10045)

insert into marks (value, lesson_id , student_id ) VALUES (10, 9391, 53)
insert into marks (value, lesson_id, student_id) VALUES ('9', 9392, 53)
insert into marks (value, lesson_id, student_id) VALUES ('8', 9393, 53)


select * from marks m WHERE student_id = 53

select * from books WHERE taken_by_student_id  = 53

SELECT s.id as student_id, 
       s.name, 
       s.second_name, 
       g.id as group_id,
       g.title as group_name, 
       g.start_date, 
       g.end_date,
       GROUP_CONCAT(DISTINCT b.id) as book_id, 
       GROUP_CONCAT(DISTINCT b.title) as book_title,
       GROUP_CONCAT(DISTINCT m.id) as mark_id,
       GROUP_CONCAT(DISTINCT m.value) as mark_value,
       GROUP_CONCAT(DISTINCT l.id) as lesson_id,
       GROUP_CONCAT(DISTINCT l.title) as lesson_title,
       GROUP_CONCAT(DISTINCT s2.id) as subject_id,
       GROUP_CONCAT(DISTINCT s2.title) as subject_title
FROM students s
LEFT JOIN `groups` g ON s.group_id = g.id
LEFT JOIN books b ON s.id = b.taken_by_student_id
LEFT JOIN marks m ON s.id = m.student_id
LEFT JOIN lessons l ON m.lesson_id = l.id
LEFT JOIN subjets s2 ON s2.id = l.subject_id
WHERE s.id = 53
GROUP BY s.id, s.name, s.second_name, g.id, g.title, g.start_date, g.end_date