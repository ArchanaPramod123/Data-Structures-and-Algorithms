def fibinocci(l):
    l2=[0,1]
    while len(l2)<l:
        next_term=l2[-1]+l2[-2]
        l2.append(next_term)
    return l2


l1=10
print(fibinocci(l1))
