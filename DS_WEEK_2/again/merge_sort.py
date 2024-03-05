def merge(l):
    if len(l)>1:
        mid=len(l)//2
        left_list=l[:mid]
        right_list=l[mid:]
        merge(left_list)
        merge(right_list)
        i=0
        j=0
        k=0
        while i<len(left_list) and j<len(right_list):
            if left_list[i]<right_list[j]:
                l[k]=left_list[i]
                i=i+1
                k=k+1
            else:
                l[k]=right_list[j]
                j=j+1
                k=k+1
        while i<len(left_list):
            l[k]=left_list[i]
            i=i+1
            k=k+1
        while j<len(right_list):
            l[k]=right_list[j]
            j=j+1
            k=k+1
l=[9,8,0,-3,67,1,3,4]
print(l)
merge(l)
print(l)

        










# def mergesort(l):
#     if len(l)>1:
#         mid=len(l)//2
#         left_list=l[:mid]
#         right_list=l[mid:]
#         mergesort(left_list)
#         mergesort(right_list)
#         i=0
#         j=0
#         k=0
#         while i<len(left_list) and j<len(right_list):
#             if left_list[i]<right_list[j]:
#                 l[k]=left_list[i]
#                 i=i+1
#                 k=k+1
#             else:
#                 l[k]=right_list[j]
#                 j=j+1
#                 k=k+1
#         while i<len(left_list):
#             l[k]=left_list[i]
#             i=i+1
#             k=k+1
#         while j<len(right_list):
#             l[k]=right_list[j]
#             j=j+1
#             k=k+1
# l=[0,-90,2,3,4,12,-27,673,23,45,3,2,1,13]
# print(l)
# mergesort(l)
# print(l)

# def mergesort(l):
#     if len(l)>1:
#         mid=len(l)//2
#         left_list=l[:mid]
#         right_list=l[mid:]
#         mergesort(left_list)
#         mergesort(right_list)
#         i=0
#         j=0
#         k=0
#         while i<len(left_list) and j<len(right_list):
#             if left_list[i]<right_list[j]:
#                 l[k]=left_list[i]
#                 i=i+1
#                 k=k+1
#             else:
#                 l[k]=right_list[j]
#                 j=j+1
#                 k=k+1
#         while i<len(left_list):
#             l[k]=left_list[i]
#             i=i+1
#             k=k+1
#         while j<len(right_list):
#             l[k]=right_list[j]
#             j=j+1
#             k=k+1
# l=[90,2,3,5,7,1,-9,0,-13,56,34]
# print(l)
# mergesort(l)
# print(l)    
