#create a node
class Node:
    #inisilize the field
    def __init__(self,data):
        self.data=data
        self.ref=None

#we create the individual nodes with the class in the link we neec to create th link of these node
class LinkedList:
    def __init__(self):
        #contain the head
        self.head=None
    def print_LL(self):
        if self.head is None:
            print('Linked list is empty')
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
LL1=LinkedList()
LL1.print_LL()

        