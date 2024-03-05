def counter(c):
    if c<=0:
        return c
    else:
        return c+counter(c-1)
res=counter(4)
print(res)

# def fact(c):
#     if c==1:
#         return 1
#     else:
#         return c*fact(c-1)
# res=fact(5)
# print(res)
    