def duplicate(list1):
    exist = set()
    duplicate = set()
    for i in list1:
        if i in exist:
            duplicate.add(i)
        else:
            exist.add(i)
    if duplicate:
        print("the duplicate are :",list(duplicate))
    else:
        print("not have any duplication",list(exist))

l=[1,2]
duplicate(l)

