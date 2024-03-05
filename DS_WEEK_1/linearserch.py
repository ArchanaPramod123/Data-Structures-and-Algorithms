def search(list1,key):
    for i in range(len(list1)):
        if key == list1[i]:
            print("the value is fount in the index ",i)
            break
    else:
        print("the key is not fount")
list1=[1,2,3,4,5,67,8,9,]
key=int(input("enter the key : "))
search(list1,key)
