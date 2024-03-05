def binary_recursion(list1,key,low,high):
    if low<=high:
        mid=(low+high)//2
        if list1[mid]==key:
            print("found index of given value",mid)
            return mid
        elif key<list1[mid]:
            return binary_recursion(list1,key,low,mid-1)
        else:
            return binary_recursion(list1,key,mid+1,high)
    else:
        print("the object is not found")
        return False
list1=[4,3,2,1,9,7,8,6]
list1.sort()
print(list1)
key=int(input("enter the value : "))
res=binary_recursion(list1,key,0,len(list1)-1)
