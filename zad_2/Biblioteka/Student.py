
class Student:
    def __init__(self, name: str, marks: int):
        self.name = name
        self.marks = marks
        self.is_passed = marks > 50

    def __str__(self):
        return f'''
            Wynik egzaminu {self.marks} % {self.is_passed}
             '''