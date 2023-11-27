import json


class Employee:

    def __init__(self,name,id):
        self.name = name
        self.id = id


    def addtoemp(self):
        with open('emp.txt','a') as emp_file:
            emp_file.write(f"Name:{self.name} Emp ID:{self.id}\n")
    @classmethod
    def resignedemp(self,name):
        with open('emp.txt','r') as emp_file:
            data = emp_file.readlines()
            print(type(data))
            for emp in data:
                if name in emp:
                    data.remove(emp)
        print(data)

    @classmethod
    def printemp(cls):
        with open('emp.txt', 'r') as emp_file:
            d = emp_file.readlines()
            for n in d:
                print(n)





a=Employee('prashant',6414)
a.addtoemp()
b=Employee('narayan',7414)
b.addtoemp()
Employee.printemp()
Employee.resignedemp('prashant')

#Employee.printemp()

