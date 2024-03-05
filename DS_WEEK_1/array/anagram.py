def element_anagram(list1,list2):
    str1=''.join(map(str,list1))
    str2=''.join(map(str,list2))

    return sorted(str1)==sorted(str2)
    
list1=[1,2,3,4]
list2=[4,2,3,1,]
if element_anagram(list1,list2):
    print(f"{list1} and {list2} is anagram")

else:
    print("not")