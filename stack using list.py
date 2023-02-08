stack=[]
def push():
    if len(stack)==n:
        print("full")
    else:
        element=input("enter the element")
        stack.append(element)
        print(stack)
def pop():
    if not stack:
        print("stack is empty")
    else:
        element=stack.pop()
        print("removed element is:",element)
        print(stack)
n=int(input("enter limit of stack"))
while(1):
    print("select option 1.push 2.pop 3.exit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        break
    else:
        print("enter correct choise")
    
