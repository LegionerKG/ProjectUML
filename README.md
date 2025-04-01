# ProjectUML

UML Class Diagram for our university course system project, and I’ll try to explain it in a simple way. It has four main parts: Student, Course, Syllabus, and Professor. It’s like a map that shows how a university system works with students, courses, and teachers.

Student: This is me (or any student). It has my name (name: str) and my student ID (student_id: int), like a unique number for me. I can join a course with enroll(course: Course) and check my ID with get_id(): int.
Course: This is the class I take, like "Math 101". It has a title (title: str), a list of students (students: list[Student]), and a syllabus (syllabus: Syllabus). I think it also has methods like enroll() and get_id(), but I might have mixed that up (it should probably add students instead).
Syllabus: This is like the plan for the course, what we’ll study. It has a name (name: str) and a student_id: int (but I’m not sure why it needs that—maybe it’s a mistake?). It also has enroll() and get_id(), but I think it should update the topics instead.
Professor: This is our teacher. They have a name (name: str) and a department (department: str), like "Computer Science". They can also enroll() and get_id(), but I think it should be something like teaching the course instead.
Connections:

The Course has many students (shown with a ◇), so I can join a course, but I can also leave and join another one.
The Course has one Syllabus (shown with a ◆), and if the course ends, the syllabus isn’t needed anymore.
The Course is taught by one Professor (shown with a line), but the professor can teach other courses too.
