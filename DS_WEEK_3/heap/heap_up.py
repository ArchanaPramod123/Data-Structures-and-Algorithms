def max_heap(a,i):
    left=(2*i)+1
    right=(2*i)+2
    if left<len(a) and a[left]>a[i]:
        largest=left
    else:
        largest=i
    if right<len(a) and a[right]>a[largest]:
        largest=right
    if largest != i:
        a[i],a[largest]=a[largest],a[i]
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


def heap_insert(a,i):
    a.append(i)
    heap_up(a,len(a)-1)

# a=[89,3,45,0,12,4,56]
a=[34,5,2,7,0,41,8]
build(a)
print(a)
heap_insert(a,100)
print(a)