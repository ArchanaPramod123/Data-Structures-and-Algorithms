def insertion(l1):
    for i in range(1,len(l1)):
        min_val=l1[i]
        min_index=i
        while min_val<l1[min_index-1] and min_index>0:
            l1[min_index]=l1[min_index-1]
            min_index=min_index-1
        l1[min_index]=min_val
l1=[0,-1,90,2,33,54,-23,-432]
print(l1)
insertion(l1)
print(l1)

# def insertion(l1):
#     for i in range(1,len(l1)):
#         min_val=l1[i]
#         min_index=i
#         while min_val<l1[min_index-1] and min_index>0:
#             l1[min_index]=l1[min_index-1]
#             min_index=min_index-1
#         l1[min_index]=min_val
# l1=[9,8,0,6,-2,23,2334,-9,-34]
# print(l1)
# insertion(l1)
# print(l1)

# def insertion(l1):
#     for i in range(1,len(l1)):
#         currect=l1[i]
#         pos=i
#         while currect<l1[pos-1] and pos>0:
#             l1[pos]=l1[pos-1]
#             pos=pos-1
#         l1[pos]=currect
# l1=[90,89,0,-1,900,2,7]
# print(l1)
# insertion(l1)
# print(l1)