def bubble(l):
    for i in range(len(l)-1,0,-1):
        for j in range(i):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
l=[90,4,3,8,9,6,1,0,-4,78]
print(l)
bubble(l)
print(l)


# def bubble(l):
#     for i in range(len(l)-1,0,-1):
#         for j in range(i):
#             if l[j]>l[j+1]:
#                 l[j],l[j+1]=l[j+1],l[j]
# l=[0,2,3,4,1,-2,34,4,8,56,9]
# print(l)
# bubble(l)
# print(l)

# def bubble_sort(l):
#     for i in range(len(l)-1,0,-1):
#         for j in range(i):
#             if l[j]>l[j+1]:
#                 l[j],l[j+1]=l[j+1],l[j]
# l=[0,90,-2,34,2,3,421,986]
# print(l)
# bubble_sort(l)
# print(l)

# def bubble_sort(l):
#     for i in range(len(l)-1,0,-1):
#         for j in range(i):
#             if l[j]>l[j+1]:
#                 l[j],l[j+1]=l[j+1],l[j]
# l=[90,3,2,4,-4,0,-12,-45,89]
# print(l)
# bubble_sort(l)
# print(l)

