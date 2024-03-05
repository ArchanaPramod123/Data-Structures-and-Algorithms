class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class CircularList:
    def __init__(self):
        self.head=None
    def print_CC(self):
        if self.head is None:
            print("empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.nref
    def