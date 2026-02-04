class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BT:
    def __init__(self, data):
        self.root = Node(data)
    
    def add_left(self, root, data):
        if root:
            root.left = Node(data)
    
    def add_right(self, root, data):
        if root:
            root.right = Node(data)
        
    def pre_order(self, root):
        if root:
            print(root.data, end=" ")
            self.pre_order(root.left)
            self.pre_order(root.right)
    
    def BFS(self, root):
        if root is None:
            return
        stack = []
        stack.append(root)
        while True:
            if len(stack) == 0 :
                return
            temp = stack.pop(0) 
            print(temp.data)
            if temp.left:
                stack.append(temp.left)
            if temp.right:
                stack.append(temp.right)
            
# Main
tree = BT(1)

tree.add_left(tree.root, 2)
tree.add_right(tree.root, 3)

tree.add_left(tree.root.left, 4)
tree.add_right(tree.root.left, 5)

tree.add_right(tree.root.left.right, 8)

tree.add_left(tree.root.right, 6)
tree.add_right(tree.root.right, 7)

tree.add_left(tree.root.right.left, 15)
tree.add_right(tree.root.right.left, 9)

# Call pre_order with root
tree.BFS(tree.root)
