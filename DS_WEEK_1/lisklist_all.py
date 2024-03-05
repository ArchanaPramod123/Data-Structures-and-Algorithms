class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class single_ll:
    def __init__(self):
        self.head=None
    def print__ll(self):
        if self.head is None:
            print("empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
    def add_beg(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node

    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n= self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node

    def add_after(self,data,x):
        n=self.head
        while n is not None:
            if x==n.data:
                break
            n=n.ref
        if n is None:
            print("not found the valaue")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node

    def add_before(self,data,x):
        if self.head is None:
            print("empty")
            return
        if self.head.data==x:
            new_node=Node(data)
            new_node.ref=self.head
            self.head=new_node
            return
        n=self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n=n.ref
        if n.ref is None:
            print("not found")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node

    def delete_beg(self):
        if self.head is None:
            print("empty")
        else:
            self.head=self.head.ref
    def delete_end(self):
        if self.head is None:
            print("emptyyyyy")
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None
    def delete_any_node(self,x):
        if self.head is None:
            print("it is the empty")
            return
        if self.head.data==x:
            self.head=self.head.ref
            return
        n=self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n=n.ref
        if n.ref is None:
            print("not found")
        else:
            n.ref=n.ref.ref
ll=single_ll()
ll.add_beg(10)
ll.add_beg(20)
ll.add_end(100)
ll.add_after(200,10)
ll.add_before(345,200)
ll.delete_beg()
ll.delete_end()
ll.delete_any_node(345)
ll.print__ll()