def insertion_half(l):
    mid=len(l)//2
    for i in range(mid+1,len(l)):
        val=l[i]
        pos=i
        while val<l[pos-1] and pos>mid:
            l[pos]=l[pos-1]
            pos=pos-1
        l[pos]=val
l=[3,4,2,900,45,23,-23,0]
print(l)
insertion_half(l)
print(l)



# def insertion_half(l):
#     mid=len(l)//2
#     print(mid)
#     for i in range(mid+1,len(l)):
#         val=l[i]
#         idx=i
#         while val<l[idx-1] and idx>mid:
#             l[idx]=l[idx-1]
#             idx=idx-1
#         l[idx]=val
# l=[3,4,2,900,45,23,-23,0]
# print(l)
# insertion_half(l)
# print(l)


# def insertion_half(l):
#     mid=len(l)//2
#     for i in range(mid+1,len(l)):
#         val=l[i]
#         pos=i
#         while val<l[pos-1] and mid>0:
#             l[pos]=l[pos-1]
#             pos=pos-1
#         l[pos]=val
# l=[90,10,670,900,87]
# print(l)
# insertion_half(l)
# print(l)