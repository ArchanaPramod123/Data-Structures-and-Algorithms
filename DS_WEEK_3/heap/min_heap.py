def min_heap(a,i):
    left=(2*i)+1
    right=(2*i)+2

    if left<len(a) and a[left]<a[i]:
        small=left
    else:
        small=i

    if right<len(a) and a[right]<a[small]:
        small=right

    if small != i:
        a[small],a[i]=a[i],a[small]
        min_heap(a,small)


def build_heap(a):
    n=(len(a)//2)-1
    for i in range(n,-1,-1):
        min_heap(a,i)


a=[9,3,423,4,5,90,23,46]
build_heap(a)
print(a)

