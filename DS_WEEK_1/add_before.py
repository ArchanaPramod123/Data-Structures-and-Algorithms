class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class LinkedList:
    def __init__(self):
        self.head=None
    def print_LL(self):
        if self.head is None:
            print("empty list")
        else:
            n=self.head
            while n is not None:
                print(n.data,end=" ")
                n=n.ref
    def add_beging(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    def add_before(self,data,x):
        if self.head is None:
            print("the list is empty")
            return
        if self.head.data == x:
            new_node=Node(data)
            new_node.ref=self.head
            self.head=new_node
            return
        n=self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n=n.ref
        if n.ref is None:
            print("object is not fount in the list")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node
LL1=LinkedList()
LL1.add_beging(100)
LL1.add_beging(200)
LL1.add_before(10,200)
LL1.print_LL()
