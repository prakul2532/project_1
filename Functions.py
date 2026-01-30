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
# function types
"""
4.) Lambda Functions:
    Create a lambda function to square a number
    Create a lambda function to check if a number is even
    Use lambda with map() to double all elements in a list
    Use lambda with filter() to get even numbers from a list
    Use lambda with sorted() to sort a list of tuples by second element
"""
number = int(input("enter the number whose square you want : "))
square_number = lambda number : number ** 2
print(square_number(number))
is_even = lambda number : number % 2 == 0
print(is_even(number))
list1 = [1,2,3]
double_elements = list(map(lambda i: i * 2,list1))
print(double_elements)
filter_odd = list(filter(lambda i: i%2!=0 , list1 ))
print(filter_odd)
list2 = [(1,2),(3,4),(5,6)]
sorted_list = sorted(list2 , key=lambda x: x[1])
print(sorted_list)
"""
5.) Recursive Functions:
    Write a recursive function to calculate factorial
    Write a recursive function to find Fibonacci sequence
    Write a recursive function to calculate power (x^n)
"""
def factorial(n):
    if n == 0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
def fibo(n):
    a=0
    b=1
    for i in range(n):
        print(a,end=",")
        a,b=b,a+b
fibo(5)
print("\n")
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

print(power(2,5))
"""
6.) Higher-Order Functions:
    Create a function apply_operation(func, numbers) that applies a function to a list
    Create a function create_multiplier(n) that returns a function multiplying by n
"""
def operation_sum(list1):
    sum = 0
    for i in list1:
        sum += i
    return sum
def apply_operation(operation_sum , numbers):
    return operation_sum(numbers)
print(apply_operation(operation_sum,[1,2,3,4]))
def function_initial():
    return 2
def create_multiplier(n):
    return n * function_initial()
print(create_multiplier(3))
# Function Scope and Decorators
"""
7.) Global vs Local Scope:
    Demonstrate global and local variables with same name
    Use global keyword to modify global variable inside function
"""
a=1
b=2
def GLOBAL():
    return f" {a} and {b} are global variables."
print(GLOBAL())
def LOCAL():
    a=3
    b=4
    return f"{a} and {b} are local variables"
print(LOCAL())
def making_use_of_global():
    global a,b
    a,b=5,6
    return f"{a} and {b} are global variables"
print(making_use_of_global())
"""
8.) Simple Decorator:
    Create a decorator timer that measures function execution time
    Create a decorator logger that logs function calls
"""
import time

def timer(func):
    def wrapper():
        start_time = time.time()
        result = func()
        end_time = time.time()
        print("Execution time:", end_time - start_time)
        return result
    return wrapper
@timer
def greet():
    return "Hello world"

print(greet())
def logger(function):
    def wrapper():
        print(f"{function.__name__} is called")
        result_output = function()
        print(result_output)
    return wrapper
@logger
def hello_world():
    return "hello world"
hello_world()
"""
9.) Decorator with Parameters:
    Create a decorator repeat(n) that repeats function execution n times
"""
def repeat(n):
    def decorater(function):
        def wrapper():
            for i in range(n):
                output_new_result = function()
                print(output_new_result)
        return wrapper
    return decorater
@repeat(3)
def greet_good_evening():
    return "Good evening"
greet_good_evening()