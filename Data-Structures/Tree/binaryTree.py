# Binary Tree(BT) is a tree that contains at most 2 children at every node

# Binary Search Tree(BST) is a BT that contains any order ex: at every node:
#       left child will be smaller than parent and right child will be greater than the parent or vice-versa


# We will implement a simple binary tree and perform some operations on it like pre-order, in-order,etc.
class BST:
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
                self.right = BST(data)
        else:
            if self.left:
                self.left.add_node(data)
            else:
                self.left = BST(data)
    
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
    
    def iterative_in_order(self):
        if self is None:
            return
        curr = self
        stack =[]
        while True:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                if len(stack) == 0:
                    return
                temp = stack.pop()
                print(temp.data)
                curr = temp.right
                
                
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
    #    min value will be the leftmost leaf node in the tree
        itr = self
        while itr.left:
            itr = itr.left
        
        return itr.data
    
    def find_max(self):
    #    max value will be the rightmost leaf node in the tree 
        itr = self
        while itr.right:
            itr = itr.right
            
        return itr.data
    
    def calculate_sum(self):
        # We can do this using recursion as well but here we will do it iteratively using stack
        # Add root node to the stack and keep popping the nodes until stack is empty. For every popped node, 
            #  add its value to sum and add its left and right child to the stack if they exist.
        # Time complexity of this algorithm is O(n) and space complexity is O(h) where h is the height of the tree.
        list = []
        list.append(self)
        sum = 0
        
        while list:
            curr = list.pop()
            sum += curr.data
            if curr.left:
                list.append(curr.left)
            if curr.right:
                list.append(curr.right)

        return sum


    def delete_node(self, val):
        # While deleting a node, we can have 3 different cases:
            # 1. Deleting a leaf node : we simply delete it and update the parent
            # 2. Deleting a node with 1 child :
                # if there is no leftchild, assign right child to current
                # if there is no right child, assign left child to current
            # 3. Deleting a node with 2 child, we have 2 options :
            #   a. find the min value from the right node and replace with current node
            #   b. find the max value from the left node and replace with current node
        if val < self.data:
            if self.left:
                self.left = self.left.delete_node(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete_node(val)
        else:
            # Case 1
            if not self.left and not self.right:
                return None
            
            # Case 2
            if not self.left:
                return self.right
            if not self.right:
                return self.left
            
            # Case 3
            #Find min_value from the right subtree
            min_val = self.right.find_min() 
            self.data = min_val
            self.right = self.right.delete_node(min_val)
        
        return self
            

# Checking

root = BST(5)

root.add_node(2)
root.add_node(7)
root.add_node(3)
root.add_node(6)

root.in_order()

# print("Iteraive")
# root.iterative_in_order()
root.delete_node(2)
# print(root.calculate_sum())
    