
def valid_para(l):
    stack=[]
    open={'(','[','{'}
    close={')',']','}'}
    dic={')':'(',']':'[','}':'{'}
    for i in l:
        if i in open:
            stack.append(i)
        elif i in close:
            if not stack or stack.pop() != dic[i]:
                return False
    return not stack
l='{[)]}'
print(l)
print(valid_para(l))


# def valid_para(l):
#     stack=[]
#     open={'[','(','{'}
#     close={']',')','}'}
#     dic={']':'[',')':'(','}':'{'}
#     for i in l:
#         if i in open:
#             stack.append(i)
#         elif i in close:
#             if not stack or stack.pop() !=dic[i]:
#                 return False
#     return not stack
    
# l='[({})]'
# print(l)
# l1=valid_para(l)
# print(l1)



# def valid_paratesis(l):
#     stack=[]
#     open={'(','[','{'}
#     close={')',']','}'}
#     dict={')':'(',']':'[','}':'{'}
#     for i in l:
#         if i in open:
#             stack.append(i)
#         elif i in close:
#             if not stack or stack.pop() != dict[i]:
#                 return False
#     return not stack
# l="{([])}"
# print(l)
# print(valid_paratesis(l))



