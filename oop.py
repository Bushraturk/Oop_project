# 06_Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series
# 1. Using self
# Assignment:
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.


# solution
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

s1 = Student("John",67)
s2 = Student("Jane", 89)
s1.display()
s2.display()


