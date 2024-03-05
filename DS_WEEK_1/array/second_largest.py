l=[1,2,3,4,9,7,6]
max_vale=l[0]
secound_max=l[1]
if secound_max>max_vale:
    max_vale,secound_max=secound_max,max_vale
for i in l[2:]:
    if i > max_vale:
        secound_max=max_vale
        max_vale=i
    if i > secound_max and i!=max_vale:
        secound_max=i
print("second max ",secound_max)
print("largest ",max_vale)