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

def build_heap(a):
    n=(len(a)//2)-1
    for i in range(n,-1,-1):
        max_heap(a,i)

def delete_heap(a,val):
    pos=a.index(val)
    last=a.pop()
    a[pos]=last
    max_heap(a,pos)
a=[2,45,12,4,78,9]
print(a)
build_heap(a)
print(a)
delete_heap(a,45)
print(a)