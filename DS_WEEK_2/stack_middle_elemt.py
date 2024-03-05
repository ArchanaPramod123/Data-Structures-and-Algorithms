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
def show(stack):
    print(stack)

stack=[]
while True:
    print("1) push 2) pop 3)pop mid 4) display 5) exit")
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
        break
    else:
        print("put valid operation")
    




# def push(stack):
#     elemnt=int(input("enter the value"))
#     stack.append(elemnt)
#     print(stack)
# def pop(stack):
#     if not stack:
#         print("empty")
#     else:
#         l=len(stack)
#         mid=l//2
#         if l%2==0:
#             mid=mid-1
#         e=stack.pop(mid)
#         print("deleted:",e)
#         print(stack)
# def show(stack):
#     print(stack)

# stack=[]
# while True:
#     print("what do you want 1) insert 2) pop 3) show 4) quit")
#     chooice=int(input("enter your chooice"))
#     if chooice==1:
#         push(stack)
#     elif chooice==2:
#         pop(stack)
#     elif chooice==3:
#         show(stack)
#     elif chooice==4:
#         break
#     else:
#         print("enter valid ")
