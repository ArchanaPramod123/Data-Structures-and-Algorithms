def insertion_sort(list1):
    for i in range(1,len(list1)):
        currect_elemnet=list1[i]
        pos=i
        while currect_elemnet<list1[pos-1] and pos>0:
            list1[pos]=list1[pos-1]
            pos=pos-1
        list1[pos]=currect_elemnet
list1=[9,0,3,1,-3]
print(list1)
insertion_sort(list1)
print(list1)