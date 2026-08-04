a=int(input('Enter the number 1: '))
b=int(input('Enter the number 2: '))
op=input("Enter the operation: ")
if op=='+':
    print(a+b)
elif op=='-':
    print(a-b)
elif op=='*':
    print(a*b)
elif op == '**':
    print(a**b)
elif op == '/' or op =='//':
    if b==0:
        print('Division by zero error')
    elif op=='/':
        print(a/b)
    else:
        print(a//b)
elif op == '%':
    print(a%b)
