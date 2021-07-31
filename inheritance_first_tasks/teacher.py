from inheritance_first_tasks.person import Person
from inheritance_first_tasks.employee import Employee

class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."

