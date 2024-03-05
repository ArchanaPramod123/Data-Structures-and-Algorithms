def heapfy(a,i):
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
        heapfy(a,largest)

def build(a):
    n=(len(a)//2)-1
    for i in range(n,-1,-1):
        heapfy(a,i)



a=[34,5,2,7,0,41,8]
build(a)
print(a)