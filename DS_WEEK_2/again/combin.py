def combine(stack,stack1):
    i=0
    j=0
    combine=[]
    while i<len(stack) and j<len(stack1):
        if stack[i]<stack1[j]:
            combine.append(stack[i])
            i=i+1
        else:
            combine.append(stack1[j])
            j=j+1
    while i<len(stack):
        combine.append(stack[i])
        i=i+1
    while j<len(stack1):
        combine.append(stack1[j])
        j=j+1
    return combine
stack=[10,20,30]
stack1=[15,25,35]
print(combine(stack,stack1))



# def combine(stack,stack1):
#     i=0
#     j=0
#     combine=[]

#     while i<len(stack) and j<len(stack1):
#         if stack[i]<stack1[j]:
#             combine.append(stack[i])
#             i=i+1
#         else:
#             combine.append(stack1[j])
#             j=j+1
#     while i < len(stack):
#         combine.append(stack[i])
#         i += 1
#     while j < len(stack1):
#         combine.append(stack1[j])
#         j += 1
#     return combine
    
     
# stack=[10,20,30]
# stack1=[15,25,35]


# print(combine(stack,stack1))

