def insertion(l):
    for i in range(1,len(l)):
        min=l[i]
        index=i
        while min<l[index-1] and index>0:
            l[index]=l[index-1]
            index=index-1
        l[index]=min
l=[90,3,2,0,-2,4,1,78]
print(l)
insertion(l)
print(l)