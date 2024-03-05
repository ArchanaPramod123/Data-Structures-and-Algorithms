
def insertion(l):
    for i in range(1,len(l)):
        val=l[i]
        pos=i
        while val<l[pos-1] and pos>0:
            l[pos]=l[pos-1]
            pos=pos-1
        l[pos]=val
l=[90,3,4,2,1,-3,-45,8,-89,23,0]
print(l)
insertion(l)
print(l)

# def insertion(l):
#     i=1
#     while i<len(l):
#         val=l[i]
#         pos=i
#         while val<l[pos-1] and pos>0:
#             l[pos]=l[pos-1]
#             pos=pos-1
#         l[pos]=val
#         i=i+1
# l=[0,3,4,2,1,-12,-3,-45,234,4,9,67]
# print(l)
# insertion(l)
# print(l)


# def insertion(l):
#     for i in range(len(l)):
#         val=l[i]
#         index=i
#         while val<l[index-1] and index>0:
#             l[index]=l[index-1]
#             index=index-1
#         l[index]=val
# l=[90,2,3,4,5,1,-2,-34,-123,34,1]
# print(l)
# insertion(l)
# print(l)


# def insertion(l):
#     i=1
#     while i<len(l):
#         val=l[i]
#         pos=i
#         while val<l[pos-1] and pos>0:
#             l[pos]=l[pos-1]
#             pos=pos-1
#         l[pos]=val
#         i=i+1
# l=[90,0,-12,4,67,1,34,9]
# print(l)
# insertion(l)
# print(l)

# def insertion(l):
#     i=1
#     while i<len(l):
#         val=l[i]
#         index=i
#         while val<l[index-1] and index>0:
#             l[index]=l[index-1]
#             index=index-1
#         l[index]=val
#         i=i+1
# l=[89,0,-2,34,1,4,78,4,5,678]
# print(l)
# insertion(l)
# print(l)

# def insertionsort(l):
#     for i in range(len(l)):
#         val=l[i]
#         indx=i
#         while val<l[indx-1] and indx>0:
#             l[indx]=l[indx-1]
#             indx=indx-1
#         l[indx]=val
# l=[90,67,-9,0,789,6,9,56]
# print(l)
# insertionsort(l)
# print(l)

