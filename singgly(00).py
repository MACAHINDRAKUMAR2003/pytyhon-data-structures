class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None;
    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node
    def print(self):
        if self.head is None:
            print('Linked list is empty')
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr=llstr+str(itr.data)+'--->'
            itr = itr.next
        print(llstr)
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
            
        itr.next = Node(data,None)
    def traversal(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    def get_length(self):
        count=0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count
    def del_at_pos(self,index):
        if index<0 or index>=self.get_length():
            raise Exception ('Invalid Index')
        if index==0:
            self.head=self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if(count==index-1):
                itr.next = itr.next.next
                break
            itr = itr.next
            count+=1
    def insert_at_any_position(self,index,data):
        if index<0 or index>=self.get_length():
            raise Exception('Invalid Index')
        if index == 0:
            self.insert_at_begining(data)
            return
        count=0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            count+=1
    def del_at_end(self):
        if(self.head != None):
          if(self.head.next == None):
            self.head = None
          else:
            temp = self.head
          while(temp.next.next != None):
              temp = temp.next
        lastNode = temp.next
        temp.next = None
        lastNode = None
    def del_at_begin(self):
        if (self.head != None):
            temp = self.head
            self.head = self.head.next
            temp = None
    def traversal(self):
        if self.head is None:
            print("Empty Doubly Linked List")
        else:
            itr=self.head
            while itr is not None:
                print(itr.data,"<===>",end="")
                itr=itr.next
            print("NULL")
sample=LinkedList()
'''''if __name__=="__main__":
    ll =LinkedList()
    ll.insert_at_beginning(["mango"])
    ll.print()
    ll.insert_at_end(["akash"])
    ll.print()
    ll.insert_at_end(["paramesh"])
    ll.print()
    ll.insert_at_end(["prakash"])
    ll.print()
    ll.insert_at(2,["mahendra"])
    ll.print()
    count = ll.get_length()
    print(count)
    ll.remove_at(1)
    ll.print()
    ll.remove_at_end()
    ll.print()
    ll.remove_at_start()
    ll.print()'''''
t='y'
while(t=='y'):
	print("Enter your chocie to perform an operation on Doubly Linked List \n1 for Adding Node\n2 for Deleting the elements in the Doubly Linked List\n3 for Displaying the elements in Doubly Linked List")
	choice=int(input())
	if choice==1:
		print("Enter the data to insert")
		data=int(input())
		s=int(input("Enter 1 to add at beginning, 2 to add at end, 3 to add at any position : "))
		if s==1:
			sample.insert_at_beginning(data) 
		elif s==2:
			sample.insert_at_end(data)
		elif s==3:
			index=int(input("Enter the index to add"))
			sample.insert_at_any_position(data,index)
		else:
			print("Invalid choice")
	
	elif choice==2:
		s=int(input("Enter 1 to delete the element at beginning, 2 for deleting at end, 3 to delete at any position : "))
		
		if s==1:
			sample.del_at_begin()
		elif s==2:
			sample.del_at_end()
		elif s==3:
			index=int(input("Enter the index to delete"))
			sample.del_at_pos(index)
		else:
			print("Invalid choice")
		
				
	elif choice==3:
		print("Elements in the Linked list are")
		sample.traversal()
		sample.print()
	
	else:
		print("Invalid choice")
			
	n=input("if you want to continue press y else any other key: ")
	t=n
	

