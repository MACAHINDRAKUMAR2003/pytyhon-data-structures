class Deque:
    def __init__(self):
        self.queue=[]
        self.count=0
    def __repr__(self):
        str = ""
        if self.count==0:
            str += "Double Ended Queue Empty."
            return str
        str += "Double Ended Queue:\n" + self.queue.__repr__()
        return str
    def insert_start(self,data):
        if self.count == 0:
            self.queue = [data,]
            self.count = 1
            return
         
        self.queue.insert(0,data)
        self.count += 1
        return
    def insert_end(self,data):
        if self.count == 0:
            self.queue = [data,]
            self.count = 1
            return
         
        self.queue.append(data)
        self.count += 1
        return
    def remove_start(self):
        if self.count == 0:
            raise ValueError("Invalid Operation")
        x = self.queue.pop(0)
        self.count -= 1
        return x
    def remove_end(self):
        if self.count == 0:
            raise ValueError("Invalid Operation")
        x = self.queue.pop()
        self.count -= 1
        return x
    def get(self, index):
        if index >= self.count | index < 0:
            raise ValueError("Index out of range.")
        return self.queue[index]
    def size(self):
        return self.count
    def display(self):
        print(self)
        return
DQ=Deque()
ch=None
print("1.insertion at staert\n  2.insetion at end\n  3.remove start\n  4.remov end\n  5.display\n  6.index\n  7.length\n  8.Exit ")
while True:
    ch=int(input("enter the choice"))
    if ch==1:
        item=int(input("enter element to de inserted"))
        DQ.insert_start(item)
    elif ch==2:
        item2=int(input("enter yte element inserted at last"))
        DQ.insert_end(item2)
    elif ch==3:
        DQ.remove_start()
    elif ch==4:
        DQ.remove_end()
    elif ch==5:
        DQ.display()
    elif ch==6:
        item3=int(input("enter index value:"))
        print(DQ.get(item3))
    elif ch==7:
        print(DQ.size())
    elif ch==8:
        print("Exit")
        break
    else:
        print("invalid operation")
        
