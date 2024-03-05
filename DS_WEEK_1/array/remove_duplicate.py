def remove(l):
    uni=list(set(l))
    l.clear()
    print(l)
    l.extend(uni)
l=[1,2,3,4,5,6,7,1,2,3]
remove(l)
print(l)