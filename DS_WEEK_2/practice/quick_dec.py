def pivot_place(list1,first,last):
    pivot=list1[last]
    left=first
    right=last-1
    while True:
        while left<=right and list1[left]<=pivot:
            left=left+1
        while left<=right and list1[right]>=pivot:
            right=right-1
        if right<left:
            break
        else:
            list1[left],list1[right]=list1[right],list1[left]
    list1[last],list1[left]=list1[left],list1[last]
    return left
def quicksort(list1,first,last):
    if first<last:
        p=pivot_place(list1,first,last)
        quicksort(list1,first,p-1)
        quicksort(list1,p+1,last)




list1=[23,5,0,-1,43,90,20]
# num=int(input("enter the size :"))
# list1=[int(input()) for x in range(num)]
print(list1)
quicksort(list1,0,len(list1)-1)
print(list1)