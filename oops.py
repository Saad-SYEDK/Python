# Object-Oriented Programming (OOP) is a programming paradigm that uses objects and classes to structure code.
# OOP allows us to model real-world entities and their interactions in a more intuitive way.

# The main principles of OOP are:

# 1. Encapsulation: The bundling of data and methods that operate on that data within a single unit (class).
    # promotes modularity and maintainability.

# 2. Inheritance: The mechanism by which one class can inherit attributes and methods from another class,
    # promoting code reusability and the creation of hierarchical relationships between classes.

# 3. Polymorphism: The ability of different classes to be treated as instances of the same class through a common interface,
        # allows flexibility and the ability to use objects of different types interchangeably.

# 4. Abstraction: The concept of hiding the complex implementation details and showing only the necessary features of an object,
    # allows for simpler interface and reducing complexity.




# Class 

# Class is a blueprint for creating objects. 
# It defines a set of attributes and methods that the created objects will have.
# A class is defined using the 'class' keyword followed by the class name and a colon.
# The class name should be in CamelCase convention.


# Object is an instance of a class. It is created using the class name followed by parentheses.
# An object can have its own attributes and methods, which are defined in the class.


# For more details and examples, look at this notes https://www.notion.so/Python-96ed6ff78c8240a79d1383120e9c1742?source=copy_link

from typing import override


class Human: # Class - Blue Print
    def __init__(self, name, gender, occupation):
        self.name = name
        self.gender = gender
        self.occupation = occupation
    
    def speak(self):
        print("Hello, my name is", self.name)
    
    def work(self):
        print("I am a", self.occupation)
    
    def sleep(self):
        print("I am sleeping..zzzz")

tc = Human("Tom Cruise", "Male", "Actor")
#Here tc is OBJECT of CLASS Human, i.e tc follows the blueprint which we defined in Human
tc.speak()
tc.work()
tc.sleep()


# Inheritance:
# Inheritance is a fundamental concept in object-oriented programming,
    # It allows a class (called a child or subclass) to inherit attributes and methods from an another class (called a parent or superclass).
# The child class can also have its own attributes and methods, and it can override the inherited methods.

class Employee(Human): # Employee is a child class of Human
    def __init__(self, name, gender, occupation, salary):
        super().__init(name,  gender, occupation) # super() is used to call the __init__ method of the parent class
        self.salary = salary
    
    @override # This is a decorator to indicate that we are overriding a method from the parent class, we will learn more about overriding in the polymorphism.
    def work(self):
        print("I am working as a", self.occupation, "and I earn", self.salary)

emp1 = Employee("Alice", "Female", "Software Engineer", 50000)
emp1.speak()
emp1.work()
emp1.sleep()

# As we can see, the Employee class inherits the speak() and sleep() methods from the Human class,
# Note: it overrides the work() method to provide a different implementation.
# we use @override decorator to indicate that we are overriding a method from the parent class.