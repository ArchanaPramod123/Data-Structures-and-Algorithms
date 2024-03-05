def baseball(l1):
    stack=[]
    for i in l1:
        if i.isdigit() or (i[0]=='-' and i[i:].isdigit()):
            stack.append(int(i))
        elif i=='D':
            stack.append(2*stack[-1])
        elif i=='+':
            stack.append(stack[-2]+stack[-1])
        elif i=='C':
            stack.pop()
        
    return sum(stack)
l1=['5','2','C','D','+']
res=baseball(l1)
print(res)