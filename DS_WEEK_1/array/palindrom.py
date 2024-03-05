# def is_palindrom(word):
#     return word == word[::-1]
# def check(l):
#     x=[word for word in l if is_palindrom(str(word))]
#     if x:
#         print("palindroms are :",x)
#     else:
#         print("not found")
# l=['anu','sonu']
# check(l)

def is_palindrom(num):
    return str(num) == str(num)[::-1]
def check(l):
    x=[num for num in l if is_palindrom(num)]
    if x:
        print("palindrom",x)
    else:
        print("not")
l=[123,454,6,7,989]
check(l)