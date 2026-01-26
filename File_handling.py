import csv
"""
BASIC FILE OPERATIONS
1.) Reading Files:
Read an entire text file and print its contents
Read a file line by line and store in a list
Read only the first 5 lines of a file
Count the number of words in a file
"""
# with open("file.txt","r") as f:
#     content = f.readlines()
# print(content[0:5])
# with open("file.txt","r") as f:
#     content2 = f.read()
#     count = 0
#     for i in content2:
#         if i in ".) ":
#             continue
#         else:
#             count += 1
#     print(count)
#-------------------------------------------------
"""
2.) Writing Files:
Create a new file and write multiple lines to it
Write a list of strings to a file (each on new line)
Append text to an existing file
"""
# with open("New_File.txt","w") as f:
#     num = int(input("enter the number of lines : "))
#     content3 = []
#     for i in range(0,num):
#         content3.append(input("enter the statement")+"\n")
#     f.writelines(content3)
#     print(content3)
#--------------------------------------------------
"""
3.) With Statement:
Use with statement to read a file
Use with statement to write to a file
"""
# with open("Create_file.txt","w") as f:
#     f.write("hello everyone")
# with open("Create_file.txt","r") as f:
#     content4 = f.read()
#     print(content4)
#---------------------------------------------------
"""
ADVANCED FILE OPERATIONS
4.) Working with CSV Files:
Read a CSV file and convert to list of dictionaries
Write a list of dictionaries to a CSV file
Append data to an existing CSV file
Read specific columns from a CSV file
"""



