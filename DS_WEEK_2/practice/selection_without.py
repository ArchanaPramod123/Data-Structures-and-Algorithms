l1=[90,9999,0,-2,-10,8,9,10000,9,-34]
print(l1)
for i in range(len(l1)):
    min_val=l1[i]
    min_index=i
    for j in range(i+1,len(l1)):
        if l1[j]<min_val:
            min_val=l1[j]
            min_index=j
    if l1[i] != l1[min_index]:
        l1[i],l1[min_index]=l1[min_index],l1[i]
print(l1)






# l1=[90,8,0,-2,3,99,1,8,-3]
# print(l1)
# for i in range(len(l1)):
#     min_val=l1[i]
#     min_index=i
#     for j in range(i+1,len(l1)):
#         if l1[j]<min_val:
#             min_val=l1[j]
#             min_index=j
#     if l1[i] != l1[min_index]:
#         l1[i],l1[min_index]=l1[min_index],l1[i]
# print(l1)

# l1=[0,99,-12,89,2,9,890,3]
# print(l1)
# for i in range(len(l1)-1):
#     min_val=l1[i]
#     min_index=i
#     for j in range(i+1,len(l1)):
#         if l1[j]<min_val:
#             min_val=l1[j]
#             min_index=j
#     if l1[i] != l1[min_index]:
#         l1[i],l1[min_index]=l1[min_index],l1[i]
# print(l1)


# l1=[90,88,92,0,-1,-20,89,278]
# print(l1)
# for i in range(len(l1)-1):
#     min_value=l1[i]
#     min_index=i
#     for j in range(i+1,len(l1)):
#         if l1[j]<min_value:
#             min_value=l1[j]
#             min_index=j
#     if l1[i] != l1[min_index]:
#         l1[i],l1[min_index]=l1[min_index],l1[i]
# print(l1)
    