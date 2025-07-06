import logging
import sys

logging.basicConfig(level=logging.ERROR, format='%(levelname)s: %(message)s', stream=sys.stdout )

def ensure_grades(method):
    def wrapper(self):
        if not self.grades:
            logging.error("Grades list is empty.")
            return ""
        return method(self)
    return wrapper


class Student:
    def __init__(self, name, age, grades = None):
        self.name = name
        self.age = age
        self.grades = grades if grades is not None else []


    @ensure_grades
    def average_grade(self):
        return sum(self.grades) / len(self.grades)



student1 = Student("Moshe",23, [100,90,80])
print(student1.average_grade())
student2 = Student("Ari",23)
print(student2.average_grade())