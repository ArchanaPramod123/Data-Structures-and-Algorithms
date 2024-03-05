class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class LinkedList:
    def __init__(self):
        self.head=None
    
    def print_LL(self):
        if self.head is None:
            print("the linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,end=" ")
                n=n.ref
    
    def add_beg(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node

    def delete_any(self,x):
        if self.head is None:
            print("then currect list is empty")
            return
        if x==self.head.data:
            self.head=self.head.ref
            return
        
        n=self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n=n.ref
        if n.ref is None:
            print("the element is not fount")
        else:
            n.ref=n.ref.ref

LL1=LinkedList()
LL1.add_beg(10)
LL1.add_beg(20)
LL1.add_beg(30)
LL1.delete_any(10)
LL1.print_LL()
