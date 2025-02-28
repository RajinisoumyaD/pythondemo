# count = 1 # called as iterators
# while count <= 5 :
#     print("drink")
#     count +=1
#     print(count)

# i = 1
# while i <=6 :
#     print ("hello", i)
#     i +=1

#print numbers from 1 to 5
# i = 5
# while i <6:
#     print(i)
#     i -= 1
    # print ("loop ended")

#1 question print numbers from 1 to 100

# i = 1
# while i<=100: # this line is called as stopping condition
#     print (i)
#     i += 1

#print numbers from 100 to 1

# i = 100
# while i >= 1:
#     print (i)
#     i -= 1

#print the multiplication table of a number n
# n = int(input("enter number : "))
# i = 1
# while i <= 10:
#     print (n*i)
#     i += 1

# print the elements of the following list using a loop: [1,4,9,16,25,36,49,64,81,100]

# nums = [1,4,9,16,25,36,49,64,81,100]
# # len(nums)

# # print (nums[0:10])
# heroes = ["hh","gg","rr","tt"]
# # traverse
# idx = 0
# while idx < len (heroes):
#     print(heroes[idx])
#     idx +=1

# search for a number x in this tuple using loop:
# nums =[1,4,9,16,25,36,49,64,81,100]

# x = 81
# i = 0 # initialization
# while i < len(nums):
#     if(nums[i] == x):
#         print ("FOUND at idx", i)
#         break
#     else:
#             print("finding..")

#     i += 1
# print ("end of loop")

# i =1
# while i <= 5:
#     print(i)
#     if (i ==3):
#         break
#     i +=1
# print("end of loop")

# i =0
# while i <=10:
#     if(i%2 !=0):
#         i +=1
#         continue #acts a s skip 
#     print(i)
#     i +=1

# list =[1,2,3,4,5]

# for val in list:
#     print(val)

# tup = (1,2,3,4,5,6,7)

# for num in tup:
#     print(num)

# str = "Rajinisoumya"

# for char in str:
#     if(char == 's'):
#         print("s found")
#         break
#     print(char)
# else:
#     print("END")

# print the elements of the following list using a loop :[1,4,9,16,25,36,49,64,81,100]
# nums = [1,4,9,16,25,36,49,64,81,100]
# for el in nums :
#     print(el)

# search for a number x in this tuple using loop:[1,4,9,16,25,36,49,64,81,100]
# nums = [1,4,9,16,25,36,49,64,81,100,49]

# x =49
# idx = 0
# for el in nums:
#     if (el ==x):
#         print("number found at idx", idx)
#         break
#     idx +=1

#Range functions
# print (range(5))
# for el in range(1,5,2):
#     print (el)
# seq = range (5)
# for i in seq:# u can also type for i in range(5)
#     print(i)


# n = int(input("enter number: "))

# for i in range (1,11):
#     print(n*i)

# Python program to display all the prime numbers within an interval

# lower = 1
# upper = 100

# print("Prime numbers between", lower, "and", upper, "are:")

# for num in range(lower, upper + 1):
# # all prime numbers are greater than 1
#  if num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             break
#     else:
#         print(num)
# for i in range (2,101,2):
#     print(i)
# for i in range(100,0,-1):
#     print(i)

#pass statement

# for i in range(5):

#     pass
# if i >5:
#         pass

# print("some useful work")

#Wap to find the sum of first n numbers.(using while)
# n = 6
# sum =0
# for i in range(n+1):
#     sum += i

#     print("total sum =", sum)

#using while
# n = 7
# sum = 0
# i = 1
# while i <=n:
#     sum +=i
#     i +=1
# print ("total sum =", sum)

#wap to find the factorial of first n numbers.(using for)
# n = 6
# fact = 1
# i = 1
# while i <= n:
#     fact *= i
#     i +=1
# print ("factorial =", fact)
# n = 5
# fact = 1
# for i in range(1, n+1):
#     fact *= i
# print ("factorial =", fact)
