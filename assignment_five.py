# Assignment Five:
# Submit your work on github for method overriding, method overloading and MRO
# MRO is Method Resolution Order, which is the order in which Python looks for a method in a hierarchy of classes
# I need two real world examples of the above concepts
# Name: ______________________
# Date: ______________________

# --- Method Overriding Example ---
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):  # Overriding the parent method
        print("Dog barks")

# Real world example 1: Vehicle base class with overridden start() in Car and Bike
class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):
    def start(self):
        print("Car is starting with a key")

class Bike(Vehicle):
    def start(self):
        print("Bike is starting with a button")

# --- Method Overloading Example (using default arguments) ---
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

# Real world example 2: Greeting with different numbers of names
class Greeter:
    def greet(self, name1, name2=None):
        if name2:
            print(f"Hello, {name1} and {name2}!")
        else:
            print(f"Hello, {name1}!")

# --- MRO (Method Resolution Order) Example ---
class A:
    def show(self):
        print("A.show()")

class B(A):
    def show(self):
        print("B.show()")

class C(A):
    def show(self):
        print("C.show()")

class D(B, C):
    pass

# D's MRO: D -> B -> C -> A

# Real world example 3: Employee, Manager, and Engineer classes
class Employee:
    def work(self):
        print("Employee working")

class Manager(Employee):
    def work(self):
        print("Manager working")

class Engineer(Employee):
    def work(self):
        print("Engineer working")

class TechLead(Manager, Engineer):
    pass

# --- Demonstration ---
print("\n--- Method Overriding ---")
d = Dog()
d.speak()
car = Car()
car.start()
bike = Bike()
bike.start()

print("\n--- Method Overloading (using default arguments) ---")
calc = Calculator()
print("Sum (2, 3):", calc.add(2, 3))
print("Sum (2, 3, 4):", calc.add(2, 3, 4))
greeter = Greeter()
greeter.greet("Alice")
greeter.greet("Alice", "Bob")

print("\n--- MRO (Method Resolution Order) ---")
d_obj = D()
d_obj.show()  # Will use B's show() due to MRO
print(D.__mro__)

tech_lead = TechLead()
tech_lead.work()  # Will use Manager's work() due to MRO
print(TechLead.__mro__)

# --- Real World Examples in Comments ---
# 1. Method Overriding: A base class 'Payment' with a method 'pay()'. Subclasses 'CreditCardPayment' and 'CashPayment' override 'pay()' to implement specific payment logic.
# 2. Method Overloading: A 'Logger' class with a 'log()' method that can accept either a message or a message and a log level (using default arguments).
# 3. MRO: In a GUI framework, a 'Widget' class is inherited by both 'Button' and 'Label', and a 'CustomButton' inherits from both. The MRO determines which 'draw()' method is called. 