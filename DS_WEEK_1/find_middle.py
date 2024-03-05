class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class single_ll:
    def __init__(self):
        self.head = None

    def print__ll(self):
        if self.head is None:
            print("empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    def add_beg(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node

    def mid_value_del(self):
        slow_ptr=self.head
        fast_ptr=self.head
        prev_ptr=None

        while fast_ptr is not None and fast_ptr.ref is not None:
            prev_ptr=slow_ptr
            slow_ptr=slow_ptr.ref
            fast_ptr=fast_ptr.ref.ref
        print("mid element is :",slow_ptr.data)
        if prev_ptr:
            prev_ptr.ref=slow_ptr.ref
        else:
            self.head=slow_ptr.ref
        
ll = single_ll()
ll.add_beg(10)
ll.add_beg(20)
ll.add_beg(30)
ll.add_beg(40)
ll.add_beg(50)
print("before delete")
print("------------")
ll.print__ll()
print("after delete ")
print("------------")
ll.mid_value_del()
ll.print__ll()
