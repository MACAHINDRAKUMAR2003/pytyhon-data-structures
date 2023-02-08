class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self,data=None):
        self.head=None
    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head=node

    def print(self):
        if self.head is None:
            print("linlkedlist is empty")
            return
        itr=self.head
        lst=''
        while itr:
            lst+=str(itr.data)+'---->'
            itr=itr.next
        print(lst)

if __name__ == '__main__':
    ll=LinkedList()
    ll.insert_at_begining(20)
    ll.insert_at_begining(30)
    ll.print()
    
    
    
