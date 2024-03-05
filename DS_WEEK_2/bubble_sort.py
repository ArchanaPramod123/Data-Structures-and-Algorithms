num=int(input("enter the length of the list :"))
l=[int(input()) for i in range(num)]
print(l)
for j in range(len(l)-1,0,-1):
    for i in range(j):
        if l[i]>l[i+1]:
            l[i],l[i+1]=l[i+1],l[i]
            print(l)
        else:
            print(l)
    print()
print(l)