# Object-Oriented Programming (OOP) in Python
# OOP is a paradigm that uses objects and classes to structure code in an intuitive, real-world manner.

# ============================================================================
# 1. CLASSES AND OBJECTS
# ============================================================================

# A Class is a blueprint for creating objects.
# An Object is an instance of a class.

class Human:  # Blueprint
    def __init__(self, name, gender, occupation):
        self.name = name
        self.gender = gender
        self.occupation = occupation
    
    def speak(self):
        print(f"Hello, my name is {self.name}")
    
    def work(self):
        print(f"I am a {self.occupation}")
    
    def sleep(self):
        print("I am sleeping...zzzzz")

# Creating objects (instances of Human class)
person1 = Human("Tom Cruise", "Male", "Actor")
person1.speak()
person1.work()

# Here person1 is an object of the Human class, with its own attributes and methods.
# Object is also called  as instances of a class. Both terms are used interchangeably in OOP.

# ============================================================================
# 2. ENCAPSULATION
# ============================================================================
# Bundling data and methods within a class, with controlled access.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute (convention: __)
    
    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited: ${amount}")
    
    def get_balance(self):  
        return self.__balance  # Controlled access

account = BankAccount("Alice", 1000)
account.deposit(500)
print(f"Balance: ${account.get_balance()}")

# ============================================================================
# 3. INHERITANCE
# ============================================================================
# A child class inherits attributes and methods from a parent class.

class Employee(Human):
    def __init__(self, name, gender, occupation, salary):
        super().__init__(name, gender, occupation)  # Call parent's __init__
        self.salary = salary
    
    def work(self):  # Override parent method
        print(f"I am working as {self.occupation} and earn ${self.salary}")

emp1 = Employee("Alice", "Female", "Software Engineer", 50000)
emp1.speak()  # Inherited from Human
emp1.work()   # Overridden method

# isinstance() checks if an object is an instance of a class or its subclasses.
# Used for OBJECTS
isinstance(emp1, Employee)  # True
isinstance(emp1, Human)     # True 

# issubclass() checks if a class is a subclass of another class.
# Used for CLASS
issubclass(Employee, Human)     # True

# MULTIPLE INHERITANCE
    # A class can inherit from multiple parent classes.
    # Research this topic


# ============================================================================
# 4. POLYMORPHISM
# ============================================================================
# Different classes can be treated as instances of the same interface.

class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")

def make_animal_speak(animal):
    animal.speak()  # Works with any object that has speak()

dog = Dog()
cat = Cat()
make_animal_speak(dog)   # Output: Woof!
make_animal_speak(cat)   # Output: Meow!
make_animal_speak(emp1)  # Output: Works with Employee too!

# ============================================================================
# 5. ABSTRACTION
# ============================================================================
# Hide complex implementation details, expose only necessary features.

from abc import ABC, abstractmethod

class Vehicle(ABC):  # Abstract class
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car engine started")
    
    def stop(self):
        print("Car engine stopped")

car = Car()
car.start()
car.stop()
