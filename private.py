# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.

# solution:

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name  # public variable
        self._salary = salary  # protected variable
        self.__ssn = ssn  # private variable

    def get_ssn(self):
        return self.__ssn

    def get_salary(self, new_salary):
        if new_salary > 0:
            self._salary = new_salary
        else:
            print("Salary must be positive in number.")

    def display(self):
        print(f"Name: {self.name}")   #public variable
        print(f"Salary: {self._salary}")   #protected variable
    
        print(f"SSN: {self.get_ssn()}")   # private variable accessed through a public method 

class Manager(Employee):
    def __init__(self, name, salary, ssn, department):
        super().__init__(name, salary, ssn)
        self.department = department  # public variable  

        def display(self):
            super().display()
            print(f"Deparment:{self.department}" )   # public variable
            print(f"Protected Salary: {self._salary}")   # protected variable
            print(f"Accessing SSN via get method: {self.get_ssn()}")

m = Manager("Ali", "12000", "123-45-6789", "IT") 
m.display() 
print(f"Department {m.department}")

m.get_salary(15000)  # Update salary using the public method
print(f"Updated Salary: {m._salary}")  # Accessing protected variable directly (not recommended)

# print(m.__ssn())
print("Prevatw SSN via managed:", m._Employee__ssn)  # This will raise an AttributeError




            






        

    