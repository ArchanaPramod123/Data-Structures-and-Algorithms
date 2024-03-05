class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class LinkedList:
    def __init__(self):
        self.head=None
    def print_LL(self):
        if self.head is None:
            print("empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref

    def list_empty_or_not(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            print("the list is not empty")

LL1=LinkedList()
LL1.list_empty_or_not(10)
LL1.list_empty_or_not(20)
LL1.print_LL()
