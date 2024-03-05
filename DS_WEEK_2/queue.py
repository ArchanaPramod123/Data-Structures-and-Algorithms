queue=[]
def enqueue():
    ele=int(input("enter the lemente"))
    queue.append(ele)
def dequeue():
    if not queue:
        print("empty")
    else:
        queue.pop(0)
def show():
    print(queue)
while True:
    print("enter the operations 1) insert 2) pop 3) display 4) exit")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        show()
    elif choice==4:
        break
    else:
        print("invalid")
    


# queue=[]
# def enqueue():
#     elemnet=int(input("enter the element"))
#     queue.append(elemnet)
#     print("the element is added")
# def dequeue():
#     if not queue:
#         print("queue is empty")
#     else:
#         e=queue.pop(0)
#         print("delete elemet is :",e)
# def show():
#     print(queue)

# while True:
#     print("enter the operations 1) insert 2) pop 3) display 4) exit")
#     choice=int(input())
#     if choice==1:
#         enqueue()
#     elif choice==2:
#         dequeue()
#     elif choice==3:
#         show()
#     elif choice==4:
#         break
#     else:
#         print("enter the valid input")