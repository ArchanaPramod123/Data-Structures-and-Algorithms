list1=[99,4,5,66,2,0,2,99]
print(list1)
for i in range(len(list1)):
    min_val=min(list1[i:])
    min_index=list1.index(min_val,i)
    if list1[i] != list1[min_index]:
        list1[i],list1[min_index]=list1[min_index],list1[i]
print(list1)