class HashTable:
    def __init__(self):
        self.MAX=100
        self.arr=[[] for i in range(self.MAX)]
    def get_hash(self,key):
        h=0
        for char in key:
            h=h+ord(char)
        return h%self.MAX
    def __setitem__(self,key,val):
        h=self.get_hash(key)
        found=False
        for index,element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][index]=(key,val)
        if not found:
            self.arr[h].append((key,val))

    def __getitem__(self,key):
        h=self.get_hash(key)
        for element in self.arr[h]:
            if element[0]==key:
                return element[1]
    def __delitem__(self,key):
        h=self.get_hash(key)
        for index,element in enumerate(self.arr[h]):
            if element[0]==key:
                del self.arr[h][index]
has=HashTable()
print(has.arr)

has["march 1"]=2
has["march 3"]=3
print("---after insert---")

print(has.arr)
del has["march 1"]
print("---after delete---")
print(has.arr)


# class Hashtable:
#     def __init__(self):
#         self.MAX=100
#         self.arr=[[] for i in range(self.MAX)]
#     def get_hash(self,key):
#         h=0
#         for char in key:
#             h=h+ord(char)
#         return h%self.MAX
#     def __setitem__(self,key,val):
#         h=self.get_hash(key)
#         found=False
#         for index,element in enumerate(key,val):
#             if len(element)==2 and element[0]==key:
#                 self.arr[h][index]=(key,val)
#                 found=True
#         if not found:
#             self.arr[h].append((key,val))
#     def __getitem__(self,key):
#         h=self.get_hash(key)
#         for element in self.arr[h]:
#             if element[0]==key:
#                 return element[1]
#     def __delitem__(self,key):
#         h=self.get_hash(key)
#         for index,element in enumerate(self.arr[h]):
#             if element[0]==key:
#                 del self.arr[h][index]    
# hash=Hashtable()
# print(hash.arr)
# hash["march 10"]=20    
# hash["march 20"]=40  
# hash["march 30"]=60  
# hash["march 40"]=80  
# print("----after insertion---------")
# print(hash.arr)
# print("----after delection---------")
# del hash["march 10"]
# print(hash.arr)





# class HashTable:
#     def __init__(self):
#         self.MAX=100
#         self.arr=[[] for i in range(self.MAX)]
#     def get_hash(self,key):
#         h=0
#         for char in key:
#             h=h+ord(char)
#         return h%self.MAX
#     def __setitem__(self,key,val):
#         h=self.get_hash(key)
#         found=False
#         for index,element in enumerate(self.arr[h]):
#             if len(element)==2 and element[0]==key:
#                 self.arr[h][index]=(key,val)
#                 found=True
#         if not found:
#             self.arr[h].append((key,val))

#     def __getitem__(self,key):
#         h=self.get_hash(key)
#         for element in self.arr[h]:
#             if element[0]==key:
#                 return element[1]
#     def __delitem__(self,key):
#         h=self.get_hash(key)
#         for index,element in enumerate(self.arr[h]):
#             if element[0]==key:
#                 del self.arr[h][index]
                
# hash=HashTable()
# print(hash.arr)
# hash['march 10']=90
# hash['march 13']=100
# hash['march 15']=110
# hash['march 17']=120
# print("-----after insertion------")
# print(hash.arr)
# del hash['march 10']
# print("-----after delection------")
# print(hash.arr)