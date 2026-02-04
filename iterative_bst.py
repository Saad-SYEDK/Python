class ItrerativeBST:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self, data):
        iterator = self
        while True:
            if iterator.data == data:
                break
            if data < iterator.data:
                if iterator.left:
                    iterator = iterator.left
                else:
                    iterator.left = ItrerativeBST(data)
                    break
            else:
                if iterator.right:
                    iterator = iterator.right
                else:
                    iterator.right = ItrerativeBST(data)
                    break
        return
    
    def pre_order_traversal(self):
        stack = []
        stack.append(self)
        while stack:
            temp = stack.pop()
            print(temp.data)
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)
        return
    def in_order_traversal(self):   
        stack = []
        i = self
        while True:
            if i:
                stack.append(i)
                i = i.left
            else: 
                if not stack:
                    break
                i = stack.pop()
                print(i.data)
                i = i.right
        return

    def post_order_traversal(self):
        stack =[]
        curr = self
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                temp = stack[-1].right
                if temp is None:
                    temp = stack.pop()
                    print(temp.data)
                    while stack and temp == stack[-1].right:
                        temp = stack.pop()
                        print(temp.data)
                else:
                    curr = temp
        return
    
    def post_order_with_visited(self):
        cur = self
        stack = [[cur,0]]
        while stack:
            temp = stack.pop()
            if temp[1] == 1:
                print(temp[0].data)
            else:
                temp[1] += 1
                stack.append(temp)
                if temp[0].right:
                    stack.append([temp[0].right,0])
                if temp[0].left:
                    stack.append([temp[0].left,0])
        return
      
        
# checking
root = ItrerativeBST(40)

elements = [30,25,35,50, 45, 60]
for elem in elements:
    root.add_child(elem)

root.pre_order_traversal()
