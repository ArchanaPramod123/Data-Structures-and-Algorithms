def search(list1,key):
    
    low=0
    high=len(list1)-1
    found=False
    
    while low<=high and not found:
        mid=(low+high)//2
        if key == list1[mid]:
            found=True
        elif key > list1[mid]:
            low = mid+1
        else:
            high = mid-1
    if found == True:
        print("found the value")
    else:
        print("not found")

list1=[8,7,5,6,4,3,2,1,9,10]
list1.sort()
print(list1)
key=int(input("enter the key value :"))

search(list1,key)
