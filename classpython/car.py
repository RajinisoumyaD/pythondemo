# class Car:
#     def __init__(self,type):
#         self.type = type
        
#     color = "black"
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped..")

# class ToyotaCar(Car):
#     def __init__(self,name,type):
#         self.name = name
#         super().__init__(type)

# car1 = ToyotaCar("pirus","electric")
# print(car1.type)

# class Fortuner(ToyotaCar):
#     def __init__(self, type):
#         self.type = type
# car1 = Fortuner("diesel")
# print(car1.start())


# car1 = ToyotaCar("Fortuner")
# car2 = ToyotaCar("prius")

# print(car1.start())
# print(car1.color)

# class method  aclass method is bound to the class and recieve the class as an implicit first argument.
# note : static method cant access or modify class state and generally for utility.
# class student:
# @class method#decorator
# def college(cls):
# pass

# class Person:
#     name = "anonymous"

#     # def changeName(self,name):
#     #     self.__class__.name = "Ravan"

#     @classmethod
#     def changeName(cls,name):
#         cls.name = name
# p1 = Person()
# p1.changeName("Ravan")
# print(p1.name)
# print(Person.name)

# class Student:
#     def __init__(self, phy,chem,math):
#         self.phy =phy
#         self.chem = chem
#         self.math = math

#     @property
#     def percentage(self):
#         return str((self.phy+self.chem+self.math)/3) + "%"

# stu1 = Student(98,97,99)
# print(stu1.percentage)

# stu1.phy=66
# print(stu1.percentage)


# class Complex:
#     def __init__(self,real,img):
#         self.real = real
#         self.img = img

#     def showNumber(self):
#         print(self.real,"i+",self.img,"j")
#     def __add__(self, num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex (newReal,newImg)

# num1 = Complex(1,3)
# num1.showNumber()

# num2 = Complex(4,6)
# num2.showNumber()
# # num3 = num1.add(num2)
# num3 = num1+num2
# num3.showNumber()
# Define a circle class to create a circle with radius r using the constructor. Define an area() method of the class which calculates the area of the circle. Define a perimeter() method of the class which allows you to calcualte the perimeter of the circle.
class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area (self):
        return (22/7) *self.radius **2
    def perimeter(self):
        return 2 * (22/7) * self.radius
    
c1 = Circle(21)
print(c1.area())
print(c1.perimeter())

# Define a Employee class with attributes role, department and salary. This class has a showDetails() method. Create an Engineer class that inherits properitites from Employee and has additional attributes :name &age.

class Employee:
    def __init__(self,role,dept,salary):
        self.role = role
        self. dept = dept
        self.salary = salary
    def showDetails(self):
        print("role =",self.role)
        print("dept=",self.dept)
        print("salary=",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Engineer","IT","75,000")
        

engg1 = Engineer("Mahesh","35",)
e1 = Employee("accountant","Finanace","60,000")
e1.showDetails()
engg1.showDetails()

# create a class called order which stores item & its price. 
# Use Dunder function__gt__() to convey that:
# order1>order2 if price of order1>price of order2

# class Order:
#     def __init__(self,item,price):
#         self.item = item
#         self.price = price

#     def __gt__(self,odr2):
#         return self.price > odr2.price
    
# odr1 = Order("chips",20)
# odr2 = Order("tea",15)

# print(odr1 < odr2)