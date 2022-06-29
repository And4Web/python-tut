class Employee:
    company = "Google"
    salary = 100

anand = Employee()
rajni = Employee()

# Creating instance attribute salary for both the objects
# anand.salary = 300
# rajni.salary = 400
anand.salary = 45
print(anand.salary)
print(rajni.salary)

# Below line throws an error as address is not present in instance/class 
# print(rajni.address) 