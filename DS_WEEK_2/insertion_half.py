# def insertion_half(l1):
#     mid=len(l1)//2
#     for i in range(mid+1,len(l1)):
#         val=l1[i]
#         index=i
#         while val<l1[index-1] and index>mid:
#             l1[index]=l1[index-1]
#             index=index-1
#         l1[index]=val
# l1=[0,90,8,3,56,2,-1,-29,244]
# print(l1)
# insertion_half(l1)
# print(l1)


# def insertion_half(l1):
#     l=len(l1)
#     mid=l//2
#     for i in range(mid+1,len(l1)):
#         current=l1[i]
#         pos=i
#         while current<l1[pos-1] and pos>mid:
#             l1[pos]=l1[pos-1]
#             pos=pos-1
#         l1[pos]=current
# l1=[22,10,60,20,-1,2]
# print(l1)
# insertion_half(l1)
# print(l1)


# def insertion_half(list1):
#     l=len(list1)
#     mid=l//2
#     for i in range(mid+1,l):
#         currect=list1[i]
#         pos=i
#         while currect<list1[pos-1] and pos>mid:
#             list1[pos]=list1[pos-1]
#             pos=pos-1
#         list1[pos]=currect

# list1=[23,5,2,0,4]
# print(list1)
# insertion_half(list1)
# print(list1)