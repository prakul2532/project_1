# Classes and objects
# Basic class
#1.) Create a class Car with attributes: brand, model, year.
class car:
    brand = "hyundai"
    model = "11203"
    year = 2005
#2.) Create an object of this class.
car().brand
car().model
car().year
#3.) Add a method display_info() that prints car details
class car:
    def display_info(self):
        brand = input("enter the brand : ")
        model = input("enter the model : ")
        year = int(input("enter the year : "))
        print(brand,model,year)
car().display_info()
# Using self keyword.
# 4.) Create a class BankAccount with:
#       Attributes: account_number, account_holder, balance
#       Methods: deposit(amount), withdraw(amount), check_balance()
#     All methods should use self to access instance variables
class BankAccount:
    def __init__(self):
        self.account_number = int(input("enter the account number : "))
        self.balance = int(input("enter the account balance : "))
        self.account_holder = input("enter the account holder : ")
    def deposit(self,amount):
        self.balance += amount
        print(f"the balance is updated by adding {amount} , and the new balance is {self.balance}")
    def withdraw(self,amount):
        self.balance -= amount
        print(f"the balance is updated by subtracting {amount} , and the new balance is {self.balance}")
    def check_balance(self):
        print(f"the current balance is {self.balance}")
# Constructor with parameters:
# 5.) Create a class Employee with:
#       __init__ method taking name, position, salary
#       Method to calculate annual salary
#       Method to give a raise (percentage increase)
class Employee:
    def __init__(self,name,position,salary):
        self.name = name
        self.position = position
        self.salary = salary
    def annual_salary(self):
         ANNUAL_SALARY = self.salary * 12
         print(f"the annual salary is {ANNUAL_SALARY}")
    def raise_salary(self,RaiseOfSalary):
        Salary_raise = self.salary * RaiseOfSalary
        print(f"the salary is {Salary_raise}")
E1 = Employee("james","manager",220000)
E1.annual_salary()
E1.raise_salary(2000)
# Inheritance
# 6.) Single Inheritance:
#   Create a base class Animal with attributes: name, species
#   Create a derived class Dog that inherits from Animal
#   Add a method bark() to Dog class
#   Use super() in Dog's constructor
class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species
class Dog(Animal):
    def __init__(self,names,species):
        super().__init__(names,species)
    def bark(self):
        print(f"the dog barking is {self.species} and his name is {self.name}")
D1 = Dog("james","labrador")
D1.bark()
# Multi-level Inheritance:
# 7.) Create: Vehicle → Car → ElectricCar
#       Each class should add its own attributes
#       Use super() appropriately
class Vehicle:
    def __init__(self,name,model):
        self.name = name
        self.model = model
class Car(Vehicle):
    def __init__(self,name,model,colour):
        super().__init__(name,model)
        self.colour = colour
class ElectricCar(Car):
    def __init__(self,name,model,colour,year):
        super().__init__(name,model,colour)
        self.year = year
E1 = ElectricCar("Hyundai",1564,"red",2014)
print(E1.name)
print(E1.model)
print(E1.year)
print(E1.colour)
# 8.) Method Overriding:
#     Create a class Shape with method area() that returns 0
#     Create subclasses Circle and Rectangle that override area()
#     Demonstrate polymorphism
class Shape:
    def area(self):
        print("0")
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        area = 3.14 * (self.radius * self.radius)
        print(area)
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        area = self.width * self.height
        print(area)
R1 = Rectangle(10,20)
R1.area()
C1 = Circle(10)
C1.area()
S1 = Shape()
S1.area()
#9.) Create a class MathOperations with:
#       A class method to convert Celsius to Fahrenheit
#       A static method to check if a number is prime
class MathOperations:
    def __init__(self,number):
        self.number = number
    def C_to_F(self):
        F = 9/5*(self.number)+32
        print(F)
    def Prime(number_check):
        count = 0
        for i in range(1, number_check + 1):
            if number_check % i == 0:
                count += 1
        if count == 2:
            print("Prime")
        else:
            print("Not Prime")
M1=MathOperations(20)
M1.C_to_F()
P1 = MathOperations
P1.Prime(3)
# Property Decorators:
#10.) Create a class Temperature with:
#       Private attribute _celsius
#       Property getter and setter with validation
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    @property
    def celsius(self):
        return self._celsius
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero (-273.15°C)")
        self._celsius = value
T1 = Temperature(273)
print(T1.celsius)
T1.celsius = 5
print(T1.celsius)
# Multiple Inheritance:
# 11.) Create classes Person and Employee
#       Create a class Manager that inherits from both
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Employee:
    def __init__(self, emp_id, salary):
        self.emp_id = emp_id
        self.salary = salary

    def show_employee_info(self):
        print(f"Employee ID: {self.emp_id}, Salary: {self.salary}")


class Manager(Person, Employee):
    def __init__(self, name, age, emp_id, salary, department):
        Person.__init__(self, name, age)
        Employee.__init__(self, emp_id, salary)
        self.department = department

    def show_manager_info(self):
        self.show_person_info()
        self.show_employee_info()
        print(f"Department: {self.department}")

m1 = Manager("Alice", 35, 101, 80000, "IT")
m1.show_manager_info()






