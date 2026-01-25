#List basic operations
#1.) create a list of 5 programming languages.
n = 5
Programming_Languages = []
for i in range(0,n):
   elements = input("enter the programming language : ")
   Programming_Languages.append(elements)
print(Programming_Languages)
#2.) Read and print the third element from the list.
print("the third element of the list is :- ",Programming_Languages[2])
#3.) update the second element to a different programming language.
new_element = input("enter the new programming language : ")
Programming_Languages[1] = new_element
print(Programming_Languages)
#4.) Delete the 4th element from the list.
Programming_Languages.pop(3)
print(Programming_Languages)
#5.) append a new Language at the end of the list.
new_element2 = input("enter the new programming language : ")
Programming_Languages.append(new_element2)
print(Programming_Languages)\
#6.) insert a new Language at the beginning of the list.
new_element3 = input("enter the new programming language : ")
Programming_Languages.insert(0,new_element3)
print(Programming_Languages)
#List Advanced operations
#1.) Create a nested list (2D list) representing a 3x3 matrix
Parent_List = []
for i in range(0,3):
    Child_List = []
    element1 = int(input("enter the first item : "))
    element2 = int(input("enter the second item : "))
    element3 = int(input("enter the third item : "))
    Child_List.append(element1)
    Child_List.append(element2)
    Child_List.append(element3)
    Parent_List.append(Child_List)
print(Parent_List)
index_wanted_row = int(input("enter the row of the element : "))
index_wanted_column = int(input("enter the column of the element : "))
index_wanted_row = index_wanted_row - 1
index_wanted_column = index_wanted_column - 1
for i in range(0,len(Parent_List)):
    if i == index_wanted_row:
        for j in range(0,len(Parent_List[i])):
            if j == index_wanted_column:
                print(Parent_List[i][j])
            else :
                continue
    else :
        continue
#2.) update an element in the nested List.
index_wanted_row = int(input("enter the row of the element : "))
index_wanted_column = int(input("enter the column of the element : "))
index_wanted_row = index_wanted_row - 1
index_wanted_column = index_wanted_column - 1
new_element4 = int(input("enter the new element : "))
for i in range(0,len(Parent_List)):
    if i == index_wanted_row:
        for j in range(0,len(Parent_List[i])):
            if j == index_wanted_column:
                Parent_List[i][j] = new_element4
                print(Parent_List)
            else :
                continue
    else :
        continue
#3.) Delete a row from the nested list.
row_number = int(input("enter the row number of the element : "))
row_number = row_number - 1
Parent_List.pop(row_number)
print(Parent_List)
#------------------------------------------------------------------
#dictionary Basic operations.
#1.) Create a dictionary representing a student with keys: name, age, grade, and subjects.
MyDict = {}
name = input("enter the name : ")
age = int(input("enter the age : "))
grade = input("enter the grade : ")
subject = input("enter the subject : ")
MyDict["name"] = name
MyDict["age"] = age
MyDict["grade"] = grade
MyDict["subject"] = subject
#2.) Read and print the student's name and age.
print(MyDict["name"],"\n",MyDict["age"])
#3.) Update the student's grade.
new_grade = input("enter the new grade : ")
MyDict["grade"] = new_grade
print(MyDict)
#4.) Delete the 'subjects' key from the dictionary.
MyDict.pop("subject")
print(MyDict)
#5.) Add a new key 'school' to the dictionary.
school = input("enter the school : ")
MyDict["school"] = school
print(MyDict)
#dictionary advanced operations.
#1.) Create a nested dictionary for multiple students.
Parent_Dictionary = {}
choice = int(input("enter the number of times : "))
for i in range(0,choice):
    Child_Dictionary={}
    name = input("enter the name : ")
    age = int(input("enter the age : "))
    Child_Dictionary["age"] = age
    grade = input("enter the grade : ")
    Child_Dictionary["grade"] = grade
    subject = input("enter the subject : ")
    Child_Dictionary["subject"] = subject
    Parent_Dictionary[name] = Child_Dictionary
print(Parent_Dictionary)
#2.) Read a specific student's information
Choice = input("enter the name of the student : ")
key_List = list(Parent_Dictionary.keys())
if Choice in Parent_Dictionary:
    print(Parent_Dictionary[Choice])
else:
    print("no such student exist")
#3.) Update a student's details.
choice_name = input("enter the name of the student : ")
if choice_name in Parent_Dictionary:
    Parent_Dictionary[choice_name]["age"] = int(input("enter the new age :"))
    Parent_Dictionary[choice_name]["grade"] = input("enter the new grade :")
    Parent_Dictionary[choice_name]["subject"] = input("enter the new subject :")
    print(f"updated dictionary :- {Parent_Dictionary}")
else :
    print(f"student {choice_name} not found")
#4.) Delete a student from the dictionary.
choice_name_delete = input("enter the name of the student : ")
Parent_Dictionary.pop(choice_name_delete)
print(Parent_Dictionary)
#5.) Find all students with grade 'A'.
for name in Parent_Dictionary:
    if Parent_Dictionary[name]["grade"] == "A":
        print(name)
    else :
        continue
#--------------------------------------------------------------------------------
#Tuples basic operations
#1.) Create a tuple with 5 different data types.
tup1=("string",2,True,2.3,[1,2,3])
#2.) Read elements using positive and negative indexing.
for i in range(0,len(tup1)):
    print(tup1[i])       #reading inside the tuple using positive indexing
for i in range(-len(tup1),-1):
    print(tup1[i])       #reading inside the tuple using negative indexing
#3.) Delete the entire tuple.
del tup1
#4.) Convert a tuple to a list, modify it, and convert back to tuple
tup2 = (1,2,3,4)
List = list(tup2)
new_list = [tup2[i]*tup2[i] for i in range(0,len(tup2))]
print(new_list,type(new_list))
new_tup = tuple(new_list)
print(new_tup,type(new_tup))
#Sets basic operations
#1.) Create two sets: set1 = {1, 2, 3, 4, 5} and set2 = {4, 5, 6, 7, 8}
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
#2.) Perform union, intersection, and difference operations.
Union = set1.union(set2)
print(Union)
Intersection = set1.intersection(set2)
print(Intersection)
Difference = set1.difference(set2)
print(Difference)
#3.) Add an element to set1.
Set1 = set1
element = int(input("enter the new element : "))
Set1.add(element)
print(Set1)
#4.) Remove an element from set2.
element_remove = int(input("enter the element to be removed : "))
Set1.remove(element_remove)
print(Set1)
#5.) Check if 3 is present in set1.
element_find = 3
if element_find in Set1:
    print("find")
else:
    print("not find")

#-------------------------------------------------------------------------
