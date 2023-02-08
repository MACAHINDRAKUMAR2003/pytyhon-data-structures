class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DoubleLinkedlist:
    def _init_(self):
        self.head=None

    def insert_at_beginning(self,data):
        newnode=node(data,self.head)
        self.head=newnode
        if self.head is none:
            self.head=newnode
        else:
            self.head=newnode
            self.head.prev=newnode
            newnode.next=self.head
    def print(self):
        if self.head is None:
            print("linled list is empty")
            return
        itr=self.head
        lst=''
        while itr:
            lst+=str(itr.data)
            itr=itr.next
        print(lst)
            
if __name__ == "__main__" :
     ll=DoubleLinkedlist()
     ll.insert_at_beginning(20)
     ll.insert_at_beginning(30)
     ll.print()

    
        
