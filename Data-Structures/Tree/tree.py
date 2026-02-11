# All the structures we saw previously were linear i.e all the elements are organized sequentially
# Now we are introducing non-linear data structure like graphs, trees,
 
# Tree - A tree is a non-linear data structure that organizes data in a hierarchical way.
# It consists of nodes connected by edges. Each node contains a value and may have child nodes.
# The topmost node is called the root, and nodes with no children are called leaves.
# Trees are used to represent relationships, such as file systems, organizational charts, and more.

# Here we will implement a simple tree structure to represent an organizational hierarchy.
# Each node will represent an employee, and the edges will represent the reporting structure.

class Employee:
    def __init__(self, name, des):
        self.name = name
        self.des= des # designation
        self.children = [] # list of child nodes (subordinates)
        self.parent = None # reference to the parent node (supervisor)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, option):
        if option == "name":
            data = self.name
        elif option == "destination":
            data = self.des
        else:
            data = self.name + " (" + self.des + ")"
        
        level = self.get_level()
        
        if level > option: # for exercise 2
            return          # for exercise 2
        spaces = ' ' * level * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + data)
        if self.children:
            for child in self.children:
                child.print_tree(option)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_product_tree():
    nilpul = Employee("Nilpul", "CEO")
    
    chinmay = Employee("Chinmay", "CTO")
    nilpul.add_child(chinmay)
    
    vishwa = Employee("Vishwa", "Infra Head")
    chinmay.add_child(vishwa)
    chinmay.add_child(Employee("Amir", "Application Head"))
    
    vishwa.add_child(Employee("Dhaval", "Cloud Manager"))
    vishwa.add_child(Employee("Abhijit", "App Manager"))

    gels = Employee("Gels", "HR Head")
    nilpul.add_child(gels)
    
    gels.add_child(Employee("Peter", "Recruitment Manager"))
    gels.add_child(Employee("Waqas", "Policy Manager"))
    
    nilpul.print_tree(4)
#Checking
build_product_tree()