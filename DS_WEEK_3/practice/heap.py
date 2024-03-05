
def max_heap(a,i):
    left=(2*i)+1
    right=(2*i)+1
    if left<len(a) and a[left]>a[i]:
        largest=left
    else:
        largest=i
    if left<len(a) and a[right]>a[largest]:
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
def inset_heap(a,i):
    a.append(i)
    heap_up(a,len(a)-1)

def delete(a,i):
    pos=a.index(i)
    last=a.pop()
    a[pos]=last
    max_heap(a,pos)




l=[20,5,6,23,1,0]
build(l)
print(l)
print("\n===insert==")
inset_heap(l,100)
print(l)
print("\n===delete==")
delete(l,0)
print(l)