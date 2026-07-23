def mul_digit(num):
    added=int("".join(map(str,num)))
    return added*len(num)
ans=mul_digit([1,2,3,4])
print(ans)
