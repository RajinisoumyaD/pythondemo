# class Student:
#     college_name = "Abc college"


#     def __init__(self,name,marks):
#         self.name = name 
#         self.marks = marks

#     def welcome(self):
#         print("welcome student,", self.name)

#     def get_marks(self):
#         return self.marks

# s1 = Student("Rajini",98)
# s1.welcome()
# print(s1.get_marks())

# Create student class that takes name and marks of 3 subjects as argument in constructor. then create a method to print the average.
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    @staticmethod
    def hello():
        print("hello")
    @staticmethod
    def college():
        print("college")

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val 
        print("hi", self.name,"your avg score is :",sum/3)

s1 = Student("Rajni",[38,49,67])
s1.hello()
s1.get_avg()

s1.college()
s1.name = "ironman"
s1.get_avg()