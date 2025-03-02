# Binary Tree(BT) is a tree that contains at most 2 children at every node

# Binary Search Tree(BST) is a BT that contains any order ex: at every node 
#       left child will be smaller than parent and right child will be greater than the parent or vice-versa

class BT:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    
    def add_node(self, data):
        if data == self.data:
            return
        
        if data > self.data:
            if self.right:
                self.right.add_node(data)
            else:
                self.right = BT(data)
        else:
            if self.left:
                self.left.add_node(data)
            else:
                self.left = BT(data)
    
    def pre_order(self):
        print(self.data)
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()
            
    def in_order(self):
        if self.left:
            self.left.in_order()
        print(self.data)
        if self.right:
            self.right.in_order()
            
    def post_order(self):
        if self.left:
            self.left.post_order()
        if self.right:
            self.right.post_order()
        print(self.data)
        
    def search(self, value) -> bool:
        if self.data  == value:
            return True
        
        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False
        else:
            if self.left:
                return self.left.search(value)
            else:
                return False
            
    def find_min(self):
        itr = self
        while itr.left:
            itr = itr.left
        
        return itr.data
    
    def find_max(self):
        itr = self
        while itr.right:
            itr = itr.right
            
        return itr.data



# Checking

root = BT(5)

root.add_node(2)
root.add_node(7)
root.add_node(3)
root.add_node(6)
root.add_node(9)

# root.post_order()

print(root.find_max())
    