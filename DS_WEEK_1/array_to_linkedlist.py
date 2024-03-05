class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print__ll(self):
        if self.head is None:
            print("empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
    def add(self,array):
        for i in array:
            new_node=Node(i)
            if self.head is None:
                self.head=new_node
            else:
                n=self.head
                while n.ref is not None:
                    n=n.ref
                n.ref=new_node
array=[1,2,3,5,6,7,8]
LL1=LinkedList()
LL1.add(array)
LL1.print__ll()

