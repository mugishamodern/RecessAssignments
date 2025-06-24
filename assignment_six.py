# Assignment Six:
# University System: Display information of Classes: Person (parent), and subclasses Student, Lecturer, Staff.
# Name: ______________________
# Date: ______________________

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course
    def display_info(self):
        super().display_info()
        print(f"Role: Student, ID: {self.student_id}, Course: {self.course}")

class Lecturer(Person):
    def __init__(self, name, age, lecturer_id, department):
        super().__init__(name, age)
        self.lecturer_id = lecturer_id
        self.department = department
    def display_info(self):
        super().display_info()
        print(f"Role: Lecturer, ID: {self.lecturer_id}, Department: {self.department}")

class Staff(Person):
    def __init__(self, name, age, staff_id, position):
        super().__init__(name, age)
        self.staff_id = staff_id
        self.position = position
    def display_info(self):
        super().display_info()
        print(f"Role: Staff, ID: {self.staff_id}, Position: {self.position}")

# Example usage:
print("--- University System Information ---")
student = Student("Alice", 20, "S123", "Computer Science")
lecturer = Lecturer("Dr. Bob", 45, "L456", "Mathematics")
staff = Staff("Carol", 35, "ST789", "Administrator")

student.display_info()
print()
lecturer.display_info()
print()
staff.display_info() 