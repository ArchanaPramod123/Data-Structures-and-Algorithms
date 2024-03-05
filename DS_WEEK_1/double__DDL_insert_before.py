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
        if self.head is None:
            print("it is empty")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data)
                n=n.pref
    

    def add_beging(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.nref=self.head
            self.head.pref=new_node
            self.head=new_node

    def add_before(self,data,x):
        
        if self.head is None:
            print("emptyyyyyyyyyyy")
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
                new_node.nref=n
                new_node.pref=n.pref
                if n.pref is not None:
                    n.pref.nref=new_node
                else:
                    self.head=new_node
                n.pref=new_node

ddl=DoubleList()
ddl.add_beging(10)
ddl.add_beging(20)
ddl.add_beging(30)
ddl.add_before(34,90)
ddl.print_f()




