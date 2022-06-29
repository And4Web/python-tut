class Employee:
    company = "Google"
    salary = 100

anand = Employee()
rajni = Employee()
anand.salary = 300
rajni.salary = 400

print(anand.company)
print(rajni.company)
Employee.company = "YouTube"
print(anand.company)
print(rajni.company)
print(anand.salary)
print(rajni.salary)