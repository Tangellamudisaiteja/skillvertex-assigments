
class Employee:
    def __init__(self, employee_id, name, department, salary):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary

    def get_info(self):
        return f"Employee ID: {self.employee_id}, Name: {self.name}, Department: {self.department}, Salary: {self.salary}"

    def increase_salary(self, percentage):
        self.salary += self.salary * (percentage / 100)

    def check_salary_threshold(self, threshold):
        return self.salary > threshold

# Creating two Employee objects
employee1 = Employee(1, "Kamal", "IT", 5000)
employee2 = Employee(2, "Srikanth", "HR", 6000)

# Displaying their information
print(employee1.get_info())
print(employee2.get_info())

# Applying a 10% raise to employee1
employee1.increase_salary(10)

# Checking if any employee has a salary higher than a certain threshold (e.g. 5500)
print(employee1.check_salary_threshold(5500))
print(employee2.check_salary_threshold(5500))

