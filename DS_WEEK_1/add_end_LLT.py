class Node:
    def __init__(self,data):
        self.data=data 
        self.ref=None
class LinkedList:
    def __init__(self):
        self.head=None

    def print_LL(self):
        if self.head is None:
            print("Empty linked list")
        else:
            n=self.head
            while n is not None:
                print(n.data,end=" ")
                n=n.ref
    
    # def add_LL(self,data):
    #     new_node=Node(data)
    #     new_node.ref=self.head
    #     self.head=new_node

    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node
                
LL1=LinkedList()
# LL1.add_LL(10)
# LL1.add_LL(30)
LL1.add_end(300)
LL1.add_end(304)
LL1.print_LL()