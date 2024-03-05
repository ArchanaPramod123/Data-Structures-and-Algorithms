def enqueue(elemnt,stack1):
    stack1.append(element)
def dequeue(stack1,stack2):
    if not stack2:
        if not stack1:
            print('empty')
        while stack1:
            stack2.append(stack1.pop())
    if not stack2:
        print("empty")
    print(stack2.pop(0))
def show(stack1,stack2):
    print("frond",stack1,"end",stack2)
stack1=[]
stack2=[]

while True:
    print("what is want 1)insert 2)delete 3)show 4)quit")
    chooise=int(input("enter your chooice"))
    if chooise==1:
        element=int(input("enter the element"))
        enqueue(element,stack1)
    elif chooise==2:
        dequeue(stack1,stack2)
    elif chooise==3:
        show(stack1,stack2)
    elif chooise==4:
        break
    else:
        print("choose a valid option")