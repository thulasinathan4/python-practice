n=input()
sum_digit=0
for i in n:
    sum_digit+=int(i)
length=len(n)
ans=sum_digit/length
print(ans)