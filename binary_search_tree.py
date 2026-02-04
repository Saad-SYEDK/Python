class BST_Node:
    def __init__(self, data):
        self.data = data
        self.left = None 
        self.right= None

    def add_child(self, data):
        if self.data == data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BST_Node(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BST_Node(data)
        return
    
    def pre_order_traversal(self):
        print(self.data)
        if self.left:
            self.left.pre_order_traversal()
        if self.right:
            self.right.pre_order_traversal()
            
    def in_order_traversal(self):   
        if self.left:
            self.left.in_order_traversal()
        print(self.data)
        if self.right:
            self.right.in_order_traversal()
    
    def post_order_traversal(self):
        if self.left:
            self.left.post_order_traversal()
        if self.right:
            self.right.post_order_traversal()
        print(self.data)
        
    def search(self, key : int) -> bool:
        if self.data == key:
            return True
        
        if self.data > key:
            if self.left:
                return self.left.search(key)
            else:
                return False
        else:
            if self.right:
                return self.right.search(key)
            else:
                return False
            
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def find_max(self):
        if not self.right:
            return self.data
        return self.right.find_max()
    
    def calculate_sum(self):
        sum = 0
        sum += self.data
        if self.left:
            sum += self.left.calculate_sum()
        if self.right:
            sum += self.right.calculate_sum()
        return sum
    
    def delete_node(self, key):
        #we have 3 cases in node deletion
        #1.leaf node - we change its parents Left/right to Null
        #2. node with only one chlid -  move its child node to its position
        #3. Node with 2 children - in this case we have to ways
            # i. find the min val   ht sub tree and replace it
            # ii. find the max value in the left sub tree and replace it
        
        if self.data > key:
            if self.left:
                self.left = self.left.delete_node(key)
        elif self.data < key:
            if self.right:
                self.right = self.right.delete_node(key)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            
            max = self.left.find_max()
            self.data = max
            self.left = self.left.delete_node(max)
#Testing Bst

root = BST_Node(40)

elements = [30,25,35,50, 45, 60]
for elem in elements:
    root.add_child(elem)

root.pre_order_traversal()
print("******")
root.in_order_traversal()
print("******")
root.post_order_traversal() 