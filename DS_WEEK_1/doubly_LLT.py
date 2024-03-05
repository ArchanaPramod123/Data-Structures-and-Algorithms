class Node:
    def __init__(self,data):
        self.data=data
        self.pref=None
        self.nref=None
class  DoubleList:
    def __init__(self):
        self.head=None

    def print_LL(self):
        if self.head is None:
            print("empty")
        else:
            n= self.head
            while n is not None:
                n=n.nref
    def print_re_LL(self):
        if self.head is None:
            print("reverese list is empty")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                n=n.pref
DDL=DoubleList()
DDL.print_re_LL()