l1=[55,-10,90,3,4,8,6,7,8,90,-1,-10,90]
print(l1)
for i in range(len(l1)):
    min_value=min(l1[i:])
    min_index=l1.index(min_value,i)
    if l1[i] != l1[min_index]:
        l1[i],l1[min_index]=l1[min_index],l1[i]
print(l1)
