# def calc_sum(a,b):
#     sum = a+b
#     print(sum)
#     return sum
# calc_sum(2,10)
# calc_sum(5,10)
# calc_sum(9,22)
# calc_sum(28,32)
# function definition
# def calc_sum(a,b): # called as parameters
#     return a+b
# sum = calc_sum(178,2221)# called as function call; called as arguments
# print(sum)

# def print_hello():
#     print("hello")
# print_hello()
# print_hello()
# print_hello()
# print_hello()

# output = print_hello()
# print(output) # prints none
# average of 3 numbers
# def calc_avg(a, b, c):

#         sum = a + b + c
#         avg = sum / 3
#         print(avg)
#         return avg
# calc_avg(90,90,66).

# print("Ra"end="$" )#sep =" "
# print("rajinisoumya")# end ="\n"

# def cal_prod(a=4,b=2):
#     print(a*b)
#     return a*b
# cal_prod(1)

#waf to print the length of a list.(list in the parameter)
# cities =["delhi","hyd","noida","pune","mbnr"]
# heroes= ["thor","raviteja","pro"]
# print(heroes[0],end="\n")
# print(heroes[1],end="\n")
# print_len(cities)
# print_len(heroes)
# waf to print the elements of a list in a single line.(list is the parameter)
# def print_len(list):
#     print(len(list))
# def print_list(list):
#     for item in list:
#         print(item,end=" ")
# print_list(cities)
# print()

#waf to find the factorial of n.(n is the parameter)
# n=5
# fact=1
# for i in range (1, n+1):
#     fact *=i
# print(fact)
# def cal_fact(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#     print(fact)
# cal_fact(6)
# waf to convert USD to INR.
# def converter(usd_val):
#     inr_val = usd_val *83
#     print(usd_val, "USD =", inr_val, "INR")
# converter(3000)

#Recursion- function calls repeteadly
# called as recursive function
# def show(n):
#     if (n ==0):# called as base case
#         return
#     print(n)
#     show(n-1)
# print("END")
# show(3)
#call stack-
# def fact(n):
#     if (n == 1 or n ==0):
#         return 1
#     return fact(n-1) * n
# print(fact(2))
#write a recursive function to calculate the sum of first n natural numbers.
# def calc_sum(n):
#     if (n ==0):
#         return 0
#     print(n)
#     return calc_sum (n-1) + n
# sum = calc_sum(10)
# print(sum)

#write a recursive function to print all elements in a list.
# Hint: use list &index as parameters.

# def print_list(list,idx = 0):
#     if (idx == len(list)):
#         return
#     print(list[idx])
#     print_list(list,idx+1)
# fruits = ["mango","banana","apple","guava"]

# print_list(fruits)