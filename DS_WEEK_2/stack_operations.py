def push(stack):
    ele=int(input("enter the element :"))
    stack.append(ele)
    print("insert element is",ele)
def pop(stack):
    if not stack:
        print("empty")
    else:
        po=stack.pop()
        print(po)
        print(stack)
def show(stack):
    if not stack:
        print("empty")
    else:
        print(stack)
stack=[]
while True:
    print("1.push 2.pop 3.display 4.exit")
    choice=int(input("enetr your choice"))
    if choice==1:
        push(stack)
    elif choice==2:
        pop(stack)
    elif choice==3:
        show(stack)
    elif choice==4:
        break
    else:
        print("enter valid choice")



# def push():
#     i=int(input("enter the element"))
#     stack.append(i)
#     print("the stack :",stack)
# def pop():
#     if not stack:
#         print("stack is empty")
#     else:
#         e=stack.pop()
#         print("after pop",e)
#         print(stack)
# stack=[]
# while True:
#     print("what do you want 1) push 2) pop 3) quit")
#     choose=int(input())
#     if choose==1:
#         push()
#     elif choose==2:
#         pop()

#     elif choose==3:
#         break
#     else:

#         print("invalid plese enter the valid opereation")
