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
        if self.key is None:
            print("empty")
            return
        if self.key==data:
            print("data found")
        elif self.key>data:
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
                    self.key=temp.key
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
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key,end=" ")
        if self.rchild:
            self.rchild.inorder()

    def min_val(self):
        current=self
        while current.lchild:
            current=current.lchild
        print("\nmin val",current.key)
    def second_largest(self):
        current=self
        while current.rchild and current.rchild.rchild:
            current=current.rchild
        print("\n secound largest",current.key)
        




def count(node):
    if node is None:
        return 0
    return 1+count(node.lchild)+count(node.rchild)

        
    
        




bts=BST(10)
l=[2,5,4,1,334]
for i in l:
    bts.insert(i)
bts.search(2)
print("\n=====before delete====")
bts.inorder()
if count(bts)>0:
    bts.delete(1,bts)
else:
    print("not possible")
print("\n=====in order====")
bts.inorder()
bts.min_val()
bts.second_largest()



