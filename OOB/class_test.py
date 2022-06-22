#!/usr/bin/python3
class Employees:
    num_emp=0
    arry_emp=[]
    def __init__(self,name:str,dept:str,toj:float,pay:float):

        Employees.num_emp+=1
        Employees.arry_emp.append(self)

        assert name !="","Must include employee name"
        assert dept !="","Must include employee department"
        assert toj != 0,"Must include time-On-Job"
        assert pay != 0,"Must include pay scale"

        self.name=name
        self.dept=dept
        self.toj=toj
        self.pay=pay
        print(f"({self.name} has been added to {self.dept} with TOJ of {self.toj} and pay of {self.pay}")
        print("Total Employees:",Employees.num_emp)

    def rm_emp(self):
        Employees.num_emp-=1
        Employees.arry_emp.remove(self)
        print(f"{self.name} has been removed")
        print("Total Employees:",Employees.num_emp)

    def pay_raise(self):
        increase=1.1
        print(f"{self.name} has received a pay increase from {self.pay} to {self.pay*increase:.2f}")
        self.pay*=increase

    def emp_bonus(self):
        bonus=.1
        print(f"{self.name} receives a yearly bonus of {self.pay*2080*bonus:.2f}")

    def chg_dept(self,dept):
        print(f"{self.name} has changed departments from {self.dept} to {dept}")
        self.dept=dept

    def print_emps():
        for e in Employees.arry_emp:
            print(e.__dict__)


Tom=Employees("Tom","ECCS",0.25,10)
Michael=Employees("Michael","ECCS",2,10)
Raj=Employees("Raj","ECCS",2.5,15)
Yesh=Employees("Yesh","ECCS",0.25,10)
David=Employees("David","ECCS",5,10)
Anil=Employees("Anil","ECCS",0.5,20)
RedShirt=Employees("Ed","ECCS",0.25,10)

Employees.rm_emp(RedShirt)
Employees.pay_raise(Anil)
Employees.emp_bonus(Anil)
Employees.emp_bonus(Tom)
Employees.chg_dept(Raj,"SRE")
Employees.chg_dept(Anil,"Executive VP")
Employees.print_emps()
