l=[9,8,7,2,1,3,4]
min_small=l[0]
second_small=l[1]
if min_small<second_small:
    second_small,min_small=min_small,second_small
for i in l[2:]:
    if i<min_small:
        second_small=min_small
        min_small=i
    if i<second_small and i!=min_small:
        second_small=i
print("second small :",second_small)
print("min small : ",min_small)