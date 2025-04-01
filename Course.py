from Student import Student
from Syllabus import Syllabus

class Course:
    def __init__(self, title: str):
        self.title = title
        self.students = []
        self.syllabus = Syllabus("Course Syllabus")
    
    def add_student(self, student: Student) -> None:
        pass
    
    def start_course(self) -> bool:
        pass
