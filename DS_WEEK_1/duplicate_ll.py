class Node:
    def __init__(self,data):
        self.data=data
        self.ref =None
class LinkedList:
    def __init__(self):
        self.head=None
    def print__LLT(self):
        if self.head is None:
            print("Empty linked list")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref

    def add(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node


    def duplicate_value(self):
        seen=set()
        n=self.head
        duplicate=set()

        while n is not None:
            if n.data in seen:
                duplicate.add(n.data)
            else:
                seen.add(n.data)
            n=n.ref
        if duplicate:
            print("duplicate elemts are",duplicate)
        else:
            print("not have duplicate value")
    def delete_duplicate(self):
        if self.head is None:
            print("empty")
            return
        seen=set()
        n=self.head
        pre=None

        while n is not None:
            if n.data in seen:
                pre.ref=n.ref
            else:
                seen.add(n.data)
                pre=n
            n=n.ref

LL1=LinkedList()
LL1.add(10)
LL1.add(20)
LL1.add(30)
LL1.add(20)
LL1.add(30)
LL1.duplicate_value()
LL1.print__LLT()
LL1.delete_duplicate()
print("after delete")

LL1.print__LLT()
        