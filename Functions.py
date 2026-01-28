# Basic Function
"""
Parameterized Functions:
1.) Create a function greet(name, message) that returns a greeting
    Create a function calculate_area(length, width) that returns area
"""
def greet(name,message):
    return f"hello {name} , {message}"
print(greet("rahul","good morning"))
def calculate_area(length,width):
    return length*width
print(calculate_area(2,3))
#------------------------------------------------------------------
"""
Default Parameters:
2.) Create a function order_food(item, quantity=1, special_instructions="")
    Demonstrate calling with different numbers of arguments
"""
def order_food(item = "" , quantity = 1 , special_instructions = ""):
    return f"your item is {item} and quantity is {quantity} , {special_instructions}"
print(order_food("veg pakoda", 2 , "hope you enjoyed our product"))
print(order_food("chilli potato",3,"Hope you enjoyed our product"))
print(order_food("veg chowmein",4,"Hope you enjoyed our product"))
#-------------------------------------------------------------------
"""
Variable Arguments:
3.) Create a function sum_all(*args) that sums any number of arguments
    Create a function print_details(**kwargs) that prints key-value pairs
"""
def sum_all(*args):
    return sum(args)
print(sum_all(1,2,3,4))
def print_details(**kwargs):
    for key in kwargs:
        print(f"{key}:{kwargs[key]}")
print_details(name="rahul",age=21,course="Bsc(hons)Electronics")
