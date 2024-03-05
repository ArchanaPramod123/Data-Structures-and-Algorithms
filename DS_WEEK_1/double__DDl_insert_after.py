class Node:
    def __init__(self,data):
        self.data=data
        self.nref=None
        self.pref=None
class DoubleList:
    def __init__(self):
        self.head=None
    def print_f(self):
        
        if self.head is None:
            print("empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,end=" ")
                n=n.nref

    def print_b(self):
        n=self.head
        if n is None:
            print("emptyyyyyyy")
        else:
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data,end=" ")
                n=n.pref
    def insert_beging(self,data):
        # n=self.head
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.nref=self.head
            self.head.pref=new_node
            self.head=new_node

    def add_after(self,data,x):
        if self.head is None:
            print("empty")
        else:
            n=self.head
            while n is not None:
                if n.data==x:
                    break
                n=n.nref
            if n is None:
                print("not found")
            else:
                new_node=Node(data)
                new_node.nref=n.nref
                new_node.pref=n
                if n.nref is not None:
                    n.nref.pref=new_node
                n.nref=new_node
                

DDL=DoubleList()
DDL.insert_beging(10)
DDL.insert_beging(20)
DDL.add_after(50,20)
DDL.print_f()
            
            
            
