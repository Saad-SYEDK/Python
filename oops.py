# Class 

# Class is a blueprint for creating objects. 
# It defines a set of attributes and methods that the created objects will have.
# A class is defined using the 'class' keyword followed by the class name and a colon.
# The class name should be in CamelCase convention.


# Object is an instance of a class. It is created using the class name followed by parentheses.
# An object can have its own attributes and methods, which are defined in the class.





# For more details and examples, look at this notes https://www.notion.so/Python-96ed6ff78c8240a79d1383120e9c1742?source=copy_link

class Human:
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
tc.speak()
tc.work()
tc.sleep()