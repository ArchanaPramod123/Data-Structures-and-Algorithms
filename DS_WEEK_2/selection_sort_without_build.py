num = int(input("enter the length of the list "))
list1= [int(input("enter value is :")) for i in range(num)]
print(list1)
for i in range(len(list1)):
    min_in=i
    for j in range(i+1,len(list1)):
        if list1[j]<list1[min_in]:
            min_in=j
    if list1[i] !=  list1[min_in]:
        list1[i],list1[min_in]=list1[min_in],list1[i]
print(list1)
    