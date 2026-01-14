class Employee:
    def __init__(self,emp_id,name,age,department,salary):
       self.emp_id=emp_id
       self.name=name
       self.age=age
       self.department= department
       self.salary=salary
    def display(self):
        print("\nEmployee Details:")
        print(f"id:{self.emp_id}")
        print(f"name:{self.name}")
        print(f"age:{self.age}")
        print(f"department:{self.department}")
        print(f"salary:{self.salary}")
        print("--------------------------")
class EmployeeManagementSystem:
    def __init__(self):
        self.employee=[]
        
    def register_employee(self):
        print("\nEmployee Registration Form")
        emp_id= input("enter employee id:")
        name=input("enter employee name:")
        age=int(input("enter age:"))
        dept=input("enter department:")
        salary=float(input("enter salary:"))
        emp=Employee(emp_id,name,age,dept,salary)
        self.employee.append(emp)
        print("\nemployee registered successfully!")
    def display_all(self):
        if not self.employee:
            print("\n no employees registered yet!")
            return
        print("\n=======registered employee=====")
        for emp in self.employee:
            emp.display()        
main=EmployeeManagementSystem()
while True:
    print("\n====employee management menu====")
    print("1. register employee")
    print("2. display all employees")
    print("3. exit")
    choice=input("enter your choice:")
    if choice=="1":
        main.register_employee()
    elif choice=="2":
        main.display_all()
    elif choice=="3":
        print("exiting program")
        break
    else:
        print("invalid choice! please try again.")