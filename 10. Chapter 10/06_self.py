class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")

anand = Employee()
anand.salary = 100000
anand.getSalary() # Employee.getSalary(harry)