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
print(Programming_Languages)
#6.) insert a new Language at the beginning of the list.
new_element3 = input("enter the new programming language : ")
Programming_Languages.insert(0,new_element3)
print(Programming_Languages)
#List Advanced operations
#Q1) Create a nested list (2D list) representing a 3x3 matrix
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

