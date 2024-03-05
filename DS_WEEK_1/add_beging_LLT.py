class Node:
    def __init__(self,data):
        self.data=data
        self.ref =None
class LinkedList:
    def __init__(self):
        self.head=None
    def print__LLT(self):
        if self.head is None:
            print("Empty linked list")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref

    def add(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node

LL1=LinkedList()
LL1.add(10)
LL1.add(20)
LL1.print__LLT()
        