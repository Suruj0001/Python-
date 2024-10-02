class Employee():
    def EmployeeId(self):
            print("Employee ID of employee: 2428")
    def Name(self):
            print("Employee 1 name is :  HARRY")

class Employee2():
    def EmployeeId(self):
            print("Employee ID of employee : 2428")
    def Name(self):
            print("Employee 2 name is : Ayush")

obj_employee1 = Employee()
obj_employee2 = Employee2()

for i in (obj_employee1,obj_employee2):
       i.EmployeeId()
       i.Name()

