# 8. The super() Function
# Assignment:
# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.



# solution 
class person:
    def __init__(self, name):
        self.name = name
        print(f"Name is {self.name}")

p1 = person("John Doe")
print(p1.name)

# Inheritance
class Teacher(person):
    def __init__(self, name, subject, salary):
        super().__init__(name)
        self.salary = salary
        self.subject = subject
        print(f"Subject is {self.subject}")
        # The super() function is used to call the constructor of the base class (person) from the derived class (Teacher).
        print(f"Salary is {self.salary}")

t1 = Teacher("John Doe", "Math", 50000)     
print(t1.name)  
print(t1.subject)
print(t1.salary)
# The super() function is used to call the constructor of the base class (person) from the derived class (Teacher). 
        