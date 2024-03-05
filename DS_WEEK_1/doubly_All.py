class node:
    def __init__(self,data) -> None:
        self.data = data
        self.nref = None
        self.pref = None
        
class double_ll:
    def __init__(self):
        self.head = None
        
        
    def print_d_ll(self):
        if self.head is None:
            print("The double linked list is empty ")
        else:
            n = self.head
            print()
            while n is not None:
                
                print(n.data,"-->", end="")
                n = n.nref
                
    def print_reverse(self):
        if self.head is None:
            print("The double linked list is empty")
        else:
            n = self.head
            print()
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data,"<--", end="",)
                n = n.pref
    
    def add_empty(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
        else:
            print("The linked list is not empty")
           
    def add_begin(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    def add_end(self,data):
        new_node  = node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n    
            new_node.nref = None 
            
             
    def add_after(self,data,x):
        new_node  = node(data)
        if self.head is None:
            print("The double linked list is empty")
        else:
            n = self.head
            while n is not None:
                
                if n.data is x:
                    break
                n = n.nref
                if n is None:
                    print("The given node cant be find")
                else:
                    new_node.nref = n.nref
                    new_node.pref = n
                    
                    if n.nref is not None:
                        n.nref.pref = new_node
                    n.nref = new_node
    
    def add_before(self,data,x):
        if self.head is None:
            print("The double linked list is empty ")
        else:
            n = self.head
            while n is not None:
                if n.data is x:
                    break
                n = n.nref
            if n is None:
                print("Given node cant be found ")
            else:        
                    
                new_node = node(data)
                new_node.nref = n
                new_node.pref = n.pref
                
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head = new_node
                n.pref = new_node
        
    def delete_begin(self):
            if self.head is None:
                print("The double linked list is empty ")
                return
            if self.head.nref is None:
                self.head = None
            else:
                self.head = self.head.nref
                self.head.pref = None
            
    def delete_end(self):
        if self.head is None:
                print("The double linked list is empty ")
                return
        if self.head.nref is None:
            self.head = None
        else:
            n = self.head
            while n.nref.nref is not None:
                n = n.nref
            
            n.nref = None
        
    def delete_by_data(self, data):
        if self.head is None:
                print("The double linked list is empty ")
                return
        if self.head.nref is None:
            if self.head.data is data:
                self.head = None
                return
        #else:
         #   print("The data cant be found in this double linked list ")
            
        if self.head.data is data:
            self.head = self.head.nref
            if self.head is not None:
                self.head.pref = None
        else:
            n = self.head 
            while n.nref is not None:
                if n.data is data:
                    break
                n = n.nref
            if n.nref is not None:   
                n.nref.pref = n.pref
                n.pref.nref = n.nref
            else:
                if n.data == data:
                    n.pref.nref = None
                else:
                    print("The data cant be found in this double linked list ")
                    
            
ll2 = double_ll()

ll2.add_begin(50)
ll2.add_begin(60)
ll2.add_end(20)
ll2.add_after(40,50)
ll2.add_before(55,50)
#ll2.delete_end()
ll2.delete_by_data(20)
ll2.print_d_ll()
ll2.print_reverse()