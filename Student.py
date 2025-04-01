from Course import Course

class Student:
    def __init__(self, name: str, student_id: int):
        self.name = name
        self.student_id = student_id
    
    def enroll(self, course: Course) -> None:
        pass
    
    def get_id(self) -> int:
        pass
