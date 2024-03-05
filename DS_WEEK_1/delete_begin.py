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
                print(n.data)
                n=n.ref

    def add_beg(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node

    def delete_begin(self):
        if self.head is None:
            print("the list is empty")
        else:
            self.head=self.head.ref

LL1=LinkedList()
LL1.add_beg(10)
LL1.add_beg(20)
LL1.delete_begin()
LL1.print_LL()