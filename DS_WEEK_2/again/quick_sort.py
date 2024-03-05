def pivot_place(l,first,last):
    pivot=l[first]
    left=first+1
    right=last
    while True:
        while left<=right and l[left]<=pivot:
            left=left+1
        while left<=right and l[right]>=pivot:
            right=right-1
        if right<left:
            break
        else:
            l[left],l[right]=l[right],l[left]
    l[first],l[right]=l[right],l[first]
    return right
def quick(l,first,last):
    if first<last:
        p=pivot_place(l,first,last)
        quick(l,first,p-1)
        quick(l,p+1,last)
l=[90,3,7,8,2,-1,2,5,67,89]
print(l)
quick(l,0,len(l)-1)
print(l)



# def pivot_place(l,first,last):
#     pivot=l[first]
#     left=first+1
#     right=last
#     while True:
#         while left<=right and l[left]<=pivot:
#             left=left+1
#         while left<=right and l[right]>=pivot:
#             right=right-1
#         if right<left:
#             break
#         else:
#             l[left],l[right]=l[right],l[left]
#     l[first],l[right]=l[right],l[first]
#     return right
# def quick(l,first,last):
#     if first<last:
#         p=pivot_place(l,first,last)
#         quick(l,first,p-1)
#         quick(l,p+1,last)
# l=[0,34,2,1,6,7,8,-3,-23]
# print(l)
# quick(l,0,len(l)-1)
# print(l)




# def pivot_place(l,first,last):
#     pivot=l[first]
#     left=first+1
#     right=last
#     while True:
#         while left<=right and l[left]<=pivot:
#             left=left+1
#         while left<=right and l[right]>=pivot:
#             right=right-1
#         if right<left:
#             break
#         else:
#             l[left],l[right]=l[right],l[left]
#     l[first],l[right]=l[right],l[first]
#     return right
# def quick_sort(l,first,last):
#     if first<last:
#         p=pivot_place(l,first,last)
#         quick_sort(l,first,p-1)
#         quick_sort(l,p+1,last)
# l=[0,34,6,5,7,2,3,-1,0,23,9,56,343]
# print(l)
# quick_sort(l,0,len(l)-1)
# print(l)


# def pivot_place(l,first,last):
#     pivot=l[first]
#     left=first+1
#     right=last
#     while True:
#         while left<=right and l[left]<=pivot:
#             left=left+1
#         while left<=right and l[right]>=pivot:
#             right=right-1
#         if right<left:
#             break
#         else:
#             l[left],l[right]=l[right],l[left]
#     l[first],l[right]=l[right],l[first]
#     return right
# def quick_sort(l,first,last):
#     if first<last:
#         p=pivot_place(l,first,last)
#         quick_sort(l,first,p-1)
#         quick_sort(l,p+1,last)
# l=[2,3,4,90,78,67,4,0,-3,-23,678,5,-4]
# print(l)
# quick_sort(l,0,len(l)-1)
# print(l)



# def pivot_place(l,first,last):
#     pivot=l[first]
#     left=first+1
#     right=last
#     while True:
#         while left<=right and l[left]<=pivot:
#             left=left+1
#         while left<=right and l[right]>=pivot:
#             right=right-1
#         if right<left:
#             break
#         else:
#             l[left],l[right]=l[right],l[left]
#     l[first],l[right]=l[right],l[first]
#     return right
# def quick_sort(l,first,last):
#     if first<last:
#         p=pivot_place(l,first,last)
#         quick_sort(l,first,p-1)
#         quick_sort(l,p+1,last)
# l=[90,3,4,-1,0,90,23,89]
# print(l)
# quick_sort(l,0,len(l)-1)
# print(l)