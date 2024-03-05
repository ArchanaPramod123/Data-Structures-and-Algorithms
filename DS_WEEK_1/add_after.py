class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class LInkedList:
    def __init__(self):
        self.head=None
    def print_LL(self):
        if self.head is None:
            print("Empty list")
        else:
            n= self.head
            while n is not None:
                print(n.data,end=' ')
                n=n.ref
    def add(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    
    def add_After(self,data,x):
        n=self.head
        while n is not None:
            if x == n.data:
                break
            n= n.ref
        if n is None:
            print("object is not in the list")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node
        
LL1=LInkedList()
LL1.add(10)
LL1.add(20)
LL1.add(30)
LL1.add_After(60,90)
LL1.print_LL()
