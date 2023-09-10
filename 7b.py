class Employee:
    def __init__(self,id,name,dept,salary):
        self.id = id
        self.name = name
        self.dept = dept
        self.salary = salary
        
    def up_salary(self):
        ch_dept = input("Enter the department for update the salary: ").strip()
        count = 0
        
        for i in emp_list:
            if i.dept.strip() == ch_dept:
                print("For Employee: ", i.name)
                i.salary = input("Enter the Salary to updatation: ")
                count += 1
                
            else:
                if count == 0:
                    print("No departments are available!")
                    pass
                
        print('Emp_id\t','Emp_name\t','Department\t','Salary')
        for k in emp_list:
            print(k.id,'\t',k.name,'\t\t',k.dept,'\t\t',k.salary)
            
emp_list = []
n = int(input("Enter the no. of Employees: "))
for i in range(n):
    id = int(input("Enter the Employee id: "))
    name = (input("Enter the Employee name: "))
    dept = (input("Enter the Employee department: "))
    salary = int(input("Enter the Employee salary: "))
    emp_list.append(Employee(id,name,dept,salary))
Employee.up_salary(emp_list)