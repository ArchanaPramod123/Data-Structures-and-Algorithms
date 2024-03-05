class Node:
    def __init__(self,data):
        self.data=data
        self.nref=None
        self.pref=None
class DoubleList:
    def __init__(self):
        self.head=None

    def print_f(self):
        if self.head is None:
            print("list ia empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,end=" ")
                n=n.nref
    
    def add_beging(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref=self.head
            self.head=new_node

    def delete_begin(self):
        if self.head is None:
            print("empty")
            return
        if self.head.nref is None:
            self.head=None
            print("after delete complete")
        else:
            self.head=self.head.nref
            self.head.pref=None
    # def delete_end(self):
    #     if self.head is None:
    #         print("empty list this")
    #         return
    #     if self.head.nref is None:
    #         self.head=None
    #         print("only one node so the deletion perform it become empty")
    #     else:
    #         n=self.head
    #         while n.nref is not None:
    #             n=n.nref
    #         n.pref.nref=None
            

    def delete_by_value(self, x):
        if self.head is None:
            print("The list is empty!")
            return

        if self.head.nref is None:
            if x == self.head.data:
                self.head = None
            else:
                print(f"{x} is not present")
            return

        if self.head.data == x:
            self.head = self.head.nref
            if self.head:
                self.head.pref = None
            return

        n = self.head
        while n.nref is not None:
            if x == n.data:
                break
            n = n.nref

        if n.nref is not None:
            n.nref.pref = n.pref
            n.pref.nref = n.nref
        else:
            if n.data == x:
                n.pref.nref = None
            else:
                print(f"{x} is not present in the list")


           
ddl=DoubleList()
ddl.add_beging(10)
ddl.add_beging(20)
ddl.add_beging(90)
ddl.add_beging(30)
ddl.add_beging(50)
# ddl.delete_begin()
# ddl.delete_end()
ddl.delete_by_value(90)
ddl.print_f()




