# Python code for above approach
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def insert_at_begin(self,data):
        node = Node(data)
        node.next = self.head
        if(self.head is not None):
            self.head.prev = node
            self.head = node

    def insert_at_last(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        itr = self.head
        while (itr.next):
            itr = itr.next
            itr.next = node
            node.prev=itr
    def insert_at_any_position(self):
        count=1
        while itr.next:
            if(count==pos-1):
                node=Node
    def display(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next

if __name__ == '__main__':
    dllist = DoublyLinkedList()
    dllist.insert_at_last(1)
    dllist.insert_at_last(2)
    dllist.insert_at_last(3)
    dllist.insert_at_last(4)
    dllist.insert_at_last(5)
    print("After insertion at tail: ")
    dllist.display()
    dllist.insert_at_begin(0)
    print("\nAfter insertion at head: ")
    dllist.display()

	# This code is contributed by ishankhandelwals.
