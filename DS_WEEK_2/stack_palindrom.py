def push(stack):
    ele=int(input("eneter the element :"))
    stack.append(ele)
    print(stack)
def pop(stack):
    if not stack:
        print("empty")
    else:
        dele=stack.pop()
        print("deleted elemnt is ",dele)
        print(stack)
def pop_mid(stack):
    temp_stack=[]
    if not stack:
        print("empty")
    mid=len(stack)//2
    for i in range(mid):
        temp_stack.append(stack.pop())
    
    mid_d=stack.pop()
    print("deleted element in the mid ",mid_d)
    while temp_stack:
        stack.append(temp_stack.pop())
def pali(stack):
    res=stack.copy()
    com=[]
    while stack:
        com.append(stack.pop())
    if res==com:
        print("it is palindrom")
    else:
        print("it is not palindrom")
def show(stack):
    print(stack)

stack=[]
while True:
    print("1) push 2) pop 3)pop mid 4) display 5) palindrom 6) exit")
    chooice=int(input("eneter your choice "))
    if chooice==1:
        push(stack)
    elif chooice==2:
        pop(stack)
    elif chooice==3:
        pop_mid(stack)
    elif chooice==4:
        show(stack)
    elif chooice==5:
        pali(stack)
    elif chooice==6:
        break
    else:
        print("put valid operation")
    

