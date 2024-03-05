class BST:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None
    def insert(self,data):
        if self.key is None:
            self.key=data
            return
        if self.key==data:
            return
        if self.key>data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=BST(data)
    def search(self,data):
        if self.key==data:
            print("the data is found")
            return
        if self.key>data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("not found")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("not found")
    def delete(self,data,curr):
        if self.key is None:
            print("empty")
            return
        if self.key>data:
            if self.lchild:
                self.lchild=self.lchild.delete(data,curr)
            else:
                print("not found")
        elif self.key<data:
            if self.rchild:
                self.rchild=self.rchild.delete(data,curr)
            else:
                print("not found")
        else:
            if self.lchild is None:
                temp=self.rchild
                if data==curr:
                    self.key=temp.key
                    self.lchild=temp.lchild
                    self.rchild=temp.rchild
                    temp=None
                    return
                self=None
                return temp
            if self.rchild is None:
                temp=self.lchild
                if data==curr:
                    self.key==temp.key
                    self.lchild=temp.lchild
                    self.rchild=temp.rchild
                    temp=None
                    return
                self=None
                return temp
            node=self.rchild
            while node.lchild:
                node=node.lchild
            self.key=node.key
            self.rchild=self.rchild.delete(node.key,curr)
        return self
    def pre_order(self):
        print(self.key,end=" ")
        if self.lchild:
            self.lchild.pre_order()
        if self.rchild:
            self.rchild.pre_order()
    def in_order(self):
        
        if self.lchild:
            self.lchild.in_order()
        print(self.key,end=" ")
        if self.rchild:
            self.rchild.in_order()
    def post_order(self):
        
        if self.lchild:
            self.lchild.post_order()
        if self.rchild:
            self.rchild.post_order()
        print(self.key,end=" ")
    def min_vale(self):
        current=self
        while current.lchild:
            current=self.lchild
        print("min:",current.key)
    def max_vale(self):
        max_val=self
        while max_val.rchild:
            max_val=max_val.rchild
        print("\nmax :",max_val.key)
            
        





def count(node):
    if node is None:
        return 0
    return 1+count(node.lchild)+count(node.rchild)



root=BST(10)
l=[3,56,34,0,12,89]
for i in l:
    root.insert(i)
root.search(90)
if count(root)>1:
    root.delete(3,root)
else:
    print("not possible")
print("---pre_order----")
root.pre_order()
print("---in_order----")
root.in_order()
print("---pre_order----")
root.post_order()
root.min_vale()
root.max_vale()

