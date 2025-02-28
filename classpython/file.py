# with open ("practice.txt","w") as f:
#     f. write ("Hi everyone\n we are learning file I/0\n")
#     f.write("using java.\n I like programming.")

# Create a new file "practice.txt" using python. Add the following data in it:
# Hi everyone
#  we are learning file I/0
# using java.
#  I like programming.

# waf that replace all occurrences of "java" with "python" in above file.

# with open ("practice.txt","r") as f:
#     data = f.read()
# new_data = data.replace("java","python")
# print(new_data)

# with open ("practice.txt","w")as f:
#     f.write(new_data)

# search if the word "learning" exists in the file or not.
# def check_for_word():

#     word= "learning"
#     with open ("practice.txt","r") as f:
#         data = f.read()
#         if(word in data):
#             print("Found")
#         else:
#             print("not found")
# check_for_word()
# WAF to find in which line of the file does the word "learning" occur first.print-1 if word not found.
# def check_for_line():
#     word = "pyq"
#     data = True
#     line_no = 1
#     with open ("practice.txt","r") as f:
#         while data:
#             data = f.readline()
#             if (word in data):
#                 print(line_no)
#                 return
#                 line_no += 1

#     return -1

# print(check_for_line())

# From a file containing numbers separated by comma, print the count of even numbers.
count = 0
with open ("practice.txt","r") as f:
    data = f.read()
    print(data)

    # num = ""
    # for i in range (len(data)):
    #     if (data[i] == ","):
    #         print(int(num))
    #         num = ""
    #     else:
    #         num += data[i]

    # another method
    num = data.split(",")
    for val in num:
        if (int(val)% 2 ==0):
            count +=1
    print(count)

