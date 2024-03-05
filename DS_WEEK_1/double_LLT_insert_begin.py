class Node:
    def __init__(self,data):
        self.data=data
        self.nref=None
        self.pref=None
class DoubleList:
    def __init__(self):
        self.head=None
    
    def print_F(self):
        if self.head is None:
            print("empty!")
        else:
            n=self.head
            while n is not None:
                print(n.data,end=" ")
                
                n=n.nref
    def print_B(self):
        print()
        if self.head is None:
            print("it is empty")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data,end=" ")
                n=n.pref

    def empty_or_not(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            print('it is not empty')
    def insert_beging_ddl(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.nref=self.head
            self.head.pref=new_node
            self.head=new_node

DDL=DoubleList()
# DDL.empty_or_not(10)
# DDL.empty_or_not(20)
DDL.insert_beging_ddl(100)
DDL.insert_beging_ddl(200)
DDL.print_F()
DDL.print_B()