# class Student:
#     def __init__(self, name, marks,age):
#         self.name = name
#         self.marks = marks
#         self.age = age
#         print("adding new student in Database..")


# s1 = Student("Rajini", "97","16")
# print(s1.name,s1.marks,s1.age)

# s2 = Student("soumya","88","18")
# print(s2.name,s2.marks,s2.age)

# class car:
#     color = "blue"
#     brand = "mercedes"
# car1 =car()
# print (car1.color)
# print (car1.brand)
# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("car started..")

# car1 = Car()
# car1.start()
# create account class with 2 attributes - balance and account no. create methods for debit,creditand printing the balance.

class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc
        # debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount,"was debited")
        print("total balance =", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs", amount, "was credited")
        print("total balance =", self.get_balance())

    def get_balance(self):
        return self.balance
acc1 = Account(10000,1234567899)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(50000)
acc1.credit(5000000)
acc1.debit(250000)
# print(acc1.balance)
# print(acc1.account_no)


