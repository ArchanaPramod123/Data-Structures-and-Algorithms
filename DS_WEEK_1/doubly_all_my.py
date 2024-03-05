class Node:
    def __init__(self,data):
        self.data=data
        self.nref=None
        self.pref=None
class doubly_ll:
    def __init__(self):
        self.head=None
    def print__dd(self):
        if self.head is None:
            print("empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.nref

    def print__back(self):
        if self.head is None:
            print("empty")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data)
                n=n.pref

    def add_beg(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            
        else:
            new_node.nref=self.head
            self.head.pref=new_node
            self.head=new_node

    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.nref=new_node
            new_node.pref=None

    def add_after(self,data,x):
        if self.head is None:
            print("empty")
        else:
            n=self.head
            while n is not None:
                if n.data==x:
                    break
                n=n.nref
            if n is None:
                print("not found")
            else:
                new_node=Node(data)
                new_node.pref=n
                new_node.nref=n.nref
                
                n.nref=new_node
                if n.nref is not None:
                    n.nref.pref=new_node

    def add_before(self,data,x):
        if self.head is None:
            print("empty")
        else:
            n=self.head
            while n is not None:
                if n.data==x:
                    break
                n=n.nref
            if n is None:
                print("not found")
            else:
                new_node=Node(data)
                new_node.nref=n
                new_node.pref=n.pref
                if n.pref is not None:
                    n.pref.nref=new_node
                else:
                    self.head=new_node
                n.pref=new_node

    def del_beg(self):
        if self.head is None:
            print("emptry")
            return
        if self.head.nref is None:
            self.head=None
        else:
            self.head=self.head.nref
            self.head.pref=None
    def del_end(self):
        if self.head is None:
            print("emptry")
            return
        if self.head.nref is None:
            self.head=None
        else:
            n=self.head
            while n.nref.nref is not None:
                n=n.nref
            n.nref=None
            
    def del_any(self,x):
        if self.head is None:
            print("empty")
            return
        if self.head.nref is None:
            if self.head.data==x:
                self.head=None
            else:
                print("not present")
        if self.head.data==x:
            self.head=self.head.nref
            self.head.pref=None
            return
        n=self.head
        while n.nref is not None:
            if x==n.data:
                break
            n=n.nref
        if n.nref is not None:
            n.nref.pref = n.pref
            n.pref.nref = n.nref
        else:
            if n.data == x:
                n.pref.nref = None
            else:
                print(f"{x} is not present in the list")

    

        


dd=doubly_ll()
dd.add_end(90)
dd.add_beg(10)
dd.add_beg(20)
dd.add_beg(40)
dd.add_end(100)
dd.add_after(89,90)
dd.add_before(33,20)
dd.del_beg()
dd.del_end()
dd.del_any(10)
dd.print__dd()
            

        


