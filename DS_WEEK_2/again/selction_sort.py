def selection(l):
    for i in range(len(l)):
        min_val=l[i]
        pos=i
        for j in range(i+1,len(l)):
            if l[j]<min_val:
                min_val=l[j]
                pos=j
        if l[i] != l[pos]:
            l[i],l[pos]=l[pos],l[i]
l=[0,34,2,1,4,6,76,4,-2,-24,890,7]
print(l)
selection(l)
print(l)


# def selection(l):
#     for i in range(len(l)):
#         val=l[i]
#         index=i
#         for j in range(i+1,len(l)):
#             if l[j]<val:
#                 val=l[j]
#                 index=j
#         if l[i] != l[index]:
#             l[i],l[index]=l[index],l[i]
# l=[90,3,4,5,723,1,2,-3,-56,234,45,5]
# print(l)
# selection(l)
# print(l)

# def selction(l):
#     i=0
#     while i<len(l):
#         val=l[i]
#         index=i
#         j=i+1
#         while j<len(l):
#             if l[j]<val:
#                 val=l[j]
#                 index=j
#             j=j+1
#         if l[i] != l[index]:
#             l[i],l[index]=l[index],l[i]
#         i=i+1
# l=[0,23,5,6,3,1,-34,-1,345,90]
# print(l)
# selction(l)
# print(l)

# def selection(l):
#     for i in range(len(l)):
#         val=l[i]
#         index=i
#         for j in range(i+1,len(l)):
#             if l[j]<val:
#                 val=l[j]
#                 index=j
#         if l[i] != l[index]:
#             l[i],l[index]=l[index],l[i]
# l=[0,29,3,45,7,12,-4,-34]
# print(l)
# selection(l)
# print(l)
            
# def selection(l):
#     i=0
#     while i<len(l):
#         val=l[i]
#         index=i
#         j=i+1
#         while j<len(l):
#             if l[j]<val:
#                 val=l[j]
#                 index=j
#             j=j+1
#         if l[i] != l[index]:
#             l[i],l[index]=l[index],l[i]
#         i=i+1
# size=int(input("enter the size :"))
# list1=[int(input()) for x in range(size)]
# print(list1)
# selection(list1)
# print(list1)