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
            print("The data is found")
            return
        if self.key>data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("the data is not found")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("the value is not found")
    def pre_order(self):
        print(self.key,end= ' ')
        if self.lchild:
            self.lchild.pre_order()
        if self.rchild:
            self.rchild.pre_order()
        
    def in_order(self):
        if self.lchild:
            self.lchild.in_order()
        print(self.key,end= ' ')
        if self.rchild:
            self.rchild.in_order()
    def post_order(self):
        if self.lchild:
            self.lchild.post_order()
        if self.rchild:
            self.rchild.post_order()
        print(self.key,end=' ')
    def delete(self,data,curr):
        if self.key is None:
            print("empty tree")
            return
        if self.key>data:
            if self.lchild:
                self.lchild=self.lchild.delete(data,curr)
            else:
                print("it is not fount")
        elif self.key<data:
            if self.rchild:
                self.rchild=self.rchild.delete(data,curr)
            else:
                print("the value is not get")
        else:
            if self.lchild is None:
                temp=self.rchild
                if data==curr:
                    self.key = temp.key
                    self.lchild=temp.lchild
                    self.rchild=temp.rchild
                    temp=None
                    return
                self=None
                return temp
            if self.rchild is None:
                temp=self.lchild
                if data==curr:
                    self.key = temp.key
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
    def min_val(self):
        current=self
        while current.lchild:
            current=current.lchild
        print("the min value of the tree is :",current.key)
    def max_val(self):
        current=self
        while current.rchild:
            current=current.rchild
        print("the max value of the tree is :",current.key)
    def secound_large(self):
        current=self
        while current.rchild and current.rchild.rchild:
            current=current.rchild
        if current.rchild:
            print("value is ",current.key)
        else:
            print("it has less than 2 children")
def count(node):
    if node is None:
        return 0
    return 1 + count(node.lchild) + count(node.rchild)

    

root=BST(10)
list1=[12,17,9,7,3,5,67,100,0]
for i in list1:
    root.insert(i)
root.search(36)
root.max_val()
root.min_val()
print("\npre_order")
root.pre_order()
print('\nin_order')
root.in_order()
print("\ncount is ",count(root))
if count(root)>1:
    root.delete(10,root.key)
else:
    print("can't delete")
print("\npost_order")

root.post_order()
root.secound_large()

