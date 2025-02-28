# # age = 28
# # if(True):
# #     print("can vote")
# #     print("can drive")

# light ="yellow"
# if(light == "red"):
#     print(stop)
# elif (light =="green"):
#     print("go")
# elif(light == "yellow"):
#     print("look")
# else:
#     print("light is broken")

# print("end of code")

# age= 28

# if(age >=18):
#     print("can vote")
# else:
#     print("cannot vote")

# marks = int(input ("enter student marks :"))

# if(marks>=90):
#     grade ="A"
# elif(marks >=80 and marks< 90):
#     grade = "B"
# elif(marks >= 70 and marks < 80):
#     grade = "c"
# else:
#     grade = "D"
# print("grade of the student ->",grade)
# nesting

# age = 34
# if(age>=18):
#     if (age>=80):
#         print("can drive")
#     else:
#          print("cannot drive")
# else:
#     print("cannot drive")

# num = int(input("enter number:"))

# if (num %2 ==0):
#     print("EVEN")
# else:
#     print("ODD")

# a = int(input("enter first number: "))
# b = int(input("enter secondnumber: "))
# c = int(input("enter third number: "))

# if (a>=b and a>=c):
#     print("First number is largest",a)
# elif(b>=c):
#     print("second number is largest",b)
# else:
#     print("third is largest",c)


# thislist = ["apple", "banana", "cherry"]
# print(thislist)

# mylist = ["apple", "banana", "cherry"]

# print(mylist[-1])

# mylist = ['apple', 'banana', 'cherry', 'orange', 'kiwi']
# print(mylist[1:4])
# mylist = ['apple', 'banana', 'cherry']
# mylist[1:2] = ['kiwi', 'mango']
# print(mylist[2])

mylist = ['apple', 'banana', 'cherry']
mylist.insert(0, 'orange')
print(mylist[1])

fruits = ['apple', 'banana', 'cherry']
tropical = ['mango', 'pineapple', 'papaya']
fruits.extend(tropical)

mylist = ['apple', 'banana', 'cherry']
mylist[0] = 'kiwi'
print(mylist[1])

mylist = ['apple', 'banana', 'cherry']
mylist.pop(1)
print(mylist)