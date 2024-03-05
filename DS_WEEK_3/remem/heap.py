def max_heap(a,i):
    left=(2*i)+1
    right=(2*i)+2
    if left<len(a) and a[left]>a[i]:
        largest=left
    else:
        largest=i
    if right<len(a) and a[right]>a[largest]:
        largest=right
    if largest!=i:
        a[largest],a[i]=a[i],a[largest]
        max_heap(a,largest)
def build(a):
    n=(len(a)//2)-1
    for i in range(n,-1,-1):
        max_heap(a,i)
def heap_up(a,n):
    while n>0:
        p=(n-1)//2
        if a[n]>a[p]:
            a[n],a[p]=a[p],a[n]
            n=p
        else:
            break

def insert(a,i):
    a.append(i)
    heap_up(a,len(a)-1)
def delte(a,i):
    pos=a.index(i)
    last=a.pop()
    a[pos]=last
    max_heap(a,pos)


l=[30,2,9,0,12]
build(l)
print(l)
insert(l,100)
print(l)
delte(l,100)
print(l)

