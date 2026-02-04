class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.parent = None
        self.children =[]

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def print_tree(self):
        spaces = ' ' * self.get_level() * 4
        prefix = spaces + "|__" if self.parent else ''
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def print_tree_extended(self, pair):
        spaces = ' ' * self.get_level() * 4
        prefix = spaces + "|__" if self.parent else ''
        print(prefix + self.data + '(' + pair.data + ')')
        if self.children and pair.children:
            for (child, pc) in zip (self.children, pair.children):
                child.print_tree_extended(pc)
    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        
        return level


nilpul = Node("Nilupul")
chinmay = Node("Chinmay")
gels = Node("Gels")

nilpul.add_child(chinmay)
nilpul.add_child(gels)

vishwa = Node("Vishwa")
chinmay.add_child(vishwa)
chinmay.add_child(Node("Aamir"))

vishwa.add_child(Node("Dhaval"))
vishwa.add_child(Node("Abhijit"))

gels.add_child(Node("Peter"))
gels.add_child(Node("Waqas"))

# nilpul.print_tree()

#designation tree

ceo = Node("CEO")
cto = Node("CTO")
hr = Node("HR Head")

ceo.add_child(cto)
ceo.add_child(hr)

ih  = Node("Infrastructure Head ")
cto.add_child(ih)
cto.add_child(Node("Application Head"))
ih.add_child(Node("Cloud Manager"))
ih.add_child(Node("App Manager"))


hr.add_child(Node("Recruitment Manager"))
hr.add_child(Node("Policy Manager"))

nilpul.print_tree_extended(ceo)

# nilpul.print_tree()
# ceo.print_tree()