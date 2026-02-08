class TreeNode:
    def __init__(self, name, des):
        self.name = name
        self.des= des
        self.children = []
        self.parent = None

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
    nilpul = TreeNode("Nilpul", "CEO")
    
    chinmay = TreeNode("Chinmay", "CTO")
    nilpul.add_child(chinmay)
    
    vishwa = TreeNode("Vishwa", "Infra Head")
    chinmay.add_child(vishwa)
    chinmay.add_child(TreeNode("Amir", "Application Head"))
    
    vishwa.add_child(TreeNode("Dhaval", "Cloud Manager"))
    vishwa.add_child(TreeNode("Abhijit", "App Manager"))

    gels = TreeNode("Gels", "HR Head")
    nilpul.add_child(gels)
    
    gels.add_child(TreeNode("Peter", "Recruitment Manager"))
    gels.add_child(TreeNode("Waqas", "Policy Manager"))
    
    nilpul.print_tree(0)
#Checking
build_product_tree()