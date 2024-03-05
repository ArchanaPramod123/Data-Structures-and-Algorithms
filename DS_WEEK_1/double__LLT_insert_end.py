class Node:
    def __init__(self,data):
        self.data=data
        self.nref=None
        self.pref=None
class DoublyList:
    def __init__(self):
        self.head=None
    def print_f(self):
        if self.head is None:
            print("emptyy")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.nref
    def print_b(self):
        if self.head is None:
            print("the list is empty")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data,end=" ")
                n=n.pref

    def insert_begin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.nref=self.head
            self.head.pref=new_node
            self.head=new_node

    def insert_end(self,data):
        
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.nref=new_node
            new_node.pref=n

DD=DoublyList()
DD.insert_begin(10)
DD.insert_begin(20)
DD.insert_end(90)
DD.insert_begin(80)
DD.print_b()