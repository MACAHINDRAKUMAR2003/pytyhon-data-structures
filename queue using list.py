queue=list()
def enqueue():
    if len(queue)==n:
        print("full")
    else:
        element=input("enter the element")
        queue.append(element)
        print(queue)
def dequeue():
    if not queue:
        print("stack is empty")
    else:
        element=queue.pop(0)
        print("removed element is:",element)
        print(queue)
n=int(input("enter limit of queue"))
while(1):
    print("select option 1.push 2.pop 3.exit")
    choice=int(input())
    if choice==1:
       enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        break
    else:
        print("enter correct choise")
 
