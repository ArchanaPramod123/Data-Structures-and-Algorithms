def upper(n):
    if len(n)>=2:
        up=n[0].upper()+n[1:-1]+n[-1].upper()
    else:
        up=n.upper()
    return up
l='arunima'
print(upper(l))