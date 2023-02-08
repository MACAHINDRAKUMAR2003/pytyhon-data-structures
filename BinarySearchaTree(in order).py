class Node:
    def __init__(self,value=None):
        self.value=value
        self.left=None
        self.right=None
class BinarySearchTree:
    def __init__(self):
        self.root=None
    def insert(self,value):
        node=Node(value)
        if self.root is None:
            self.root=node
        else:
            current=self.root
            while True:
                if value<current.value:
                    if current.left is None:
                        current.left=node
                        break
                    else:
                        current=current.left
                else:
                    if current.right is None:
                        current.right=node
                        break
                    else:
                        current=current.right
    def in_order_traverse(self):
        current=self.root
        stack=[]
        while True:
            if current is not None:
                stack.append(current)
                current=current.left
            else:
                current=stack.pop()
                print(current)
                current=current.right
ll=BinarySearchTree()
ll.insert(14)
ll.insert(17)
ll.insert(19)
ll.insert(7)
ll.insert(27)
ll.in_order_traverse()
                
        
        
        
