l1=[0,56,7,9,3,4,-9,5,6-134]
print(l1)
for i in range(len(l1)-1,0,-1):
    for j in range(i):
        if l1[j]>l1[j+1]:
            l1[j],l1[j+1]=l1[j+1],l1[j]
print(l1)

# l1=[0,44,2,3,6,7,8,93,2,1,-4,-5]
# print(l1)
# for i in range(len(l1)-1,0,-1):
#     for j in range(i):
#         if l1[j]>l1[j+1]:
#             l1[j],l1[j+1]=l1[j+1],l1[j]
# print(l1)


# list1=[444,45,6,7,8,444,-1,9]
# print(list1)
# for j in range(len(list1)-1,0,-1):
#     for i in range(j):
#         if list1[i]>list1[i+1]:
#             list1[i],list1[i+1]=list1[i+1],list1[i]
# print(list1)