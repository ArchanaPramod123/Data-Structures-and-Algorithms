def search(list1,key):
    list2=[]
    flag=False
    for i in range(len(list1)):
        if key == list1[i]:
            flag=True
            list2.append(i)
    if flag==True:
        for i in list2:
            print(i)
    else:
        print("key not found")

list1=[1,2,3,41,5,6,7,8,1]
key=int(input("enter the value : "))
search(list1,key)