def pivot_place(l1,first,last):
    pivot=l1[first]
    left=first+1
    right=last
    while True:
        while left<=right and l1[left]<=pivot:
            left=left+1
        while left<=right and l1[right]>=pivot:
            right=right-1
        if right<left:
            break
        else:
            l1[left],l1[right]=l1[right],l1[left]
    l1[first],l1[right]=l1[right],l1[first]
    return right
def quick(l1,first,last):
    if first<last:
        p=pivot_place(l1,first,last)
        quick(l1,first,p-1)
        quick(l1,p+1,last)
l1=[0,34,5,7,11,2,3,4,-3,-23]
print(l1)
quick(l1,0,len(l1)-1)
print(l1)


# def pivot_place(l1,first,last):
#     pivot=l1[first]
#     left=first+1
#     right=last
#     while True:
#         while left<=right and l1[left]<=pivot:
#             left=left+1
#         while left<=right and l1[right]>=pivot:
#             right=right-1
#         if right<left:
#             break
#         else:
#             l1[left],l1[right]=l1[right],l1[left]
#     l1[first],l1[right]=l1[right],l1[first]
#     return right
# def quicksort(l1,first,last):
#     if first<last:
#         p=pivot_place(l1,first,last)
#         quicksort(l1,first,p-1)
#         quicksort(l1,p+1,last)
# l1=[90,4,-9,0,456,3,67,12,-19,-1]
# print(l1)
# quicksort(l1,0,len(l1)-1)
# print(l1)




# def pivot_place(l1,first,last):
#     pivot=l1[first]
#     left=first+1
#     right=last
#     while True:
#         while left<=right and l1[left]<=pivot:
#             left=left+1
#         while left<=right and l1[right]>=pivot:
#             right=right-1
#         if right<left:
#             break
#         else:
#             l1[left],l1[right]=l1[right],l1[left]
#             # print(l1)
#     l1[first],l1[right]=l1[right],l1[first]
#     return right
# def quicksort(l1,first,last):
#     if first<last:
#         p=pivot_place(l1,first,last)
#         quicksort(l1,first,p-1)
#         quicksort(l1,p+1,last)
# l1=[89,3,0,45,6,-3,2,44,677,3,88]
# print(l1)
# quicksort(l1,0,len(l1)-1)
# print(l1)

# def pivot_place(list1,first,last):
#     pivot=list1[first]
#     left=first+1
#     right=last

#     while True:
#         while left<=right and list1[left]<=pivot:
#             left=left+1
#         while left<=right and list1[right]>=pivot:
#             right=right-1
#         if right<left:
#             break
#         else:
#             list1[left],list1[right]=list1[right],list1[left]
#         print(list1)
#     list1[first],list1[right]=list1[right],list1[first]
#     print(list1)
#     return right

# def quicksort(list1,first,last):
#     if first<last:
#         p=pivot_place(list1,first,last)
#         quicksort(list1,first,p-1)
#         quicksort(list1,p+1,last)
#         print(list1)

# list1=[53,26,93,17,31,44]
# print(list1)
# l=len(list1)
# quicksort(list1,0,l-1)
# print(list1)