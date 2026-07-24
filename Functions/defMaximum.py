def find_max(a,b,c):
    if a>b and a>c:
        return a
    elif b>c:
        return b
    else:
        return c
print(find_max(3,5,7))