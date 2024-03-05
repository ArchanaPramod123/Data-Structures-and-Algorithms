class HashTable:
    def __init__(self):
        self.MAX=100
        self.arr=[[] for i in range(self.MAX)]

    def get_hash(self,key):
        h=0
        for char in key:
            h=h+ord(char)
        print("h",h)
        print("hi",h%self.MAX)
        return h%self.MAX
        
    def __setitem__(self,key,val):
        h=self.get_hash(key)
        found=False
        for index,elemnt in enumerate(self.arr[h]):
            print('index',index)
            print('ele',elemnt)

            if len(elemnt)==2 and elemnt[0]==key:
                self.arr[h][index]=(key,val)
                found=True
                break
        if not found:
            self.arr[h].append((key,val))
    def __getitem__(self,key):
        h=self.get_hash(key)
        for element in self.arr[h]:
            if element[0]==key:
                return element[1]
        # return self.arr[h]
    def __delitem__(self,key):
        h=self.get_hash(key)
        # self.arr[h]=None
        for index,elemnet in enumerate(self.arr[h]):
            if elemnet[0]==key:
                del self.arr[h][index]
has=HashTable()
# has['march 6']=2
has['march 6']=17
has['march 1']=29
has['march 2']=500
has['march 3']=1000
has['march 4']=20
has['march 17']=6
has['march 5']=44
has['march 500']=555
del has['march 3']
# print(has.get_hash('march 6'))
# print(has.get_hash('march 17'))
# print(has.get_hash('march 7'))
# print(has.get_hash('march 8'))
# print(has.get_hash('march 9'))
# print(has.get_hash('march 10'))
# print(has.get_hash('march 11'))
# print(has.get_hash('march 12'))
# print(has.get_hash('march 13'))
# print(has.get_hash('march 14'))
# print(has.get_hash('march 200'))
# print(has.get_hash('march 300'))
# print(has.get_hash('march 33'))
# print(has.get_hash('march 400'))
# print(has.get_hash('march 500'))
# print(has.get_hash('march 4'))
# print(has.get_hash('march 1'))
print(has["march 1"])
print(has["march 6"])
print(has.arr)
del has['march 500']
print(has.arr)

