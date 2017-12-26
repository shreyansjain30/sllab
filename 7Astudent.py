class student:
    usn=" "
    name=" "
    marks1=0
    marks2=0
    marks3=0
    def __init__(self,usn,name,marks1,marks2,marks3):
        self.usn=usn
        self.name=name
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3
    def calc(self):
        print("the total is :",(self.marks1+self.marks2+self.marks3))
    def printdetail(self):
        print("Name : \n ",self.name)
        print("USN  \n ",self.usn)
        print("marks : \n ",self.marks1,self.marks2,self.marks3)
name=input("enter name ")
usn=input("enter usn ")
m1=int(input("enter the marks 1 "))
m2=int(input("enter the marks 2 "))
m3=int(input("enter the marks 3 "))
s1=student(usn,name,m1,m2,m3)
s1.calc()
s1.printdetail()