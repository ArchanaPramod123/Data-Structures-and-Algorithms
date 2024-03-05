def mergesort(l1):
    if len(l1)>1:
        mid=len(l1)//2
        left_list=l1[:mid]
        right_list=l1[mid:]
        mergesort(left_list)
        mergesort(right_list)
        i=0
        j=0
        k=0
        while i<len(left_list) and j<len(right_list):
            if left_list[i]<right_list[j]:
                l1[k]=left_list[i]
                i=i+1
                k=k+1

            else:
                l1[k]=right_list[j]
                j=j+1
                k=k+1
        while i<len(left_list):
            l1[k]=left_list[i]
            i=i+1
            k=k+1
        while j<len(right_list):
            l1[k]=right_list[j]
            j=j+1
            k=k+1
l1=[90,7,8,6,5,34,-6,0,3,4]
print(l1)
mergesort(l1)
print(l1)
# def mergesort(l1):
#     if len(l1)>1:
#         mid=len(l1)//2
#         left=l1[:mid]
#         right=l1[mid:]
#         mergesort(left)
#         mergesort(right)
#         i=0
#         j=0
#         k=0
#         while i<len(left) and j<len(right):
#             if left[i]<right[j]:
#                 l1[k]=left[i]
#                 i=i+1
#                 k=k+1
#             else:
#                 l1[k]=right[j]
#                 j=j+1
#                 k=k+1
#         while i<len(left):
#             l1[k]=left[i]
#             i=i+1
#             k=k+1
#         while j<len(right):
#             l1[k]=right[j]
#             j=j+1
#             k=k+1
# l1=[90,8,0,-1,990,7,18]
# print(l1)
# mergesort(l1)
# print(l1)

# def mergesort(list1):
#     if len(list1)>1:
#         mid=(len(list1))//2
#         left_list=list1[:mid]
#         right_list=list1[mid:]
#         mergesort(left_list)
#         mergesort(right_list)
#         i=0
#         j=0
#         k=0
#         while i<len(left_list) and j<len(right_list):
#             if left_list[i]<right_list[j]:
#                 list1[k]=left_list[i]
#                 i=i+1
#                 k=k+1
#             else:
#                 list1[k]=right_list[j]
#                 j=j+1
#                 k=k+1
#         while i<len(left_list):
#             list1[k]=left_list[i]
#             i=i+1
#             k=k+1
#         while j<len(right_list):
#             list1[k]=right_list[j]
#             j=j+1
#             k=k+1

# num=int(input("enter the size :"))
# list1=[int(input()) for x in range(num)]
# print(list1)
# mergesort(list1)
# print(list1)