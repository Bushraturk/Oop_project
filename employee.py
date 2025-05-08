# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

# The Department class should have a method to add an Employee and a method to display all Employees in the Department.
# The Employee class should have attributes for name and position.
# Implement the classes and demonstrate their functionality.

# solution
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __str__(self):
        return f"Employee Name: {self.name}, Position: {self.position}"


class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []  # ✅ Correct spelling

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_employees(self):
        print(f"Employees in {self.department_name}:")
        for employee in self.employees:
            print(employee)


# Example usage
if __name__ == "__main__":
    emp1 = Employee("Alice", "Manager")
    emp2 = Employee("Bob", "Developer")
    emp3 = Employee("Charlie", "Designer")

    department = Department("IT Department")
    department.add_employee(emp1)
    department.add_employee(emp2)
    department.add_employee(emp3)

    department.display_employees()
