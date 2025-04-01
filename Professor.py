from Course import Course

class Professor:
    def __init__(self, name: str, department: str):
        self.name = name
        self.department = department
    
    def teach_course(self, course: Course) -> None:
        pass
