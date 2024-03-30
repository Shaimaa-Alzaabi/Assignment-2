class Staff:
    def __init__(self, name, role, salary, employment_date):
        self.name = name
        self.role = role
        self.salary = salary
        self.employment_date = employment_date

    def __str__(self):
        return f"Staff: {self.name}, Role: {self.role}, Salary: {self.salary}, Employment Date: {self.employment_date}"
