while True:
    print("********WELCOME TO SIMPLE CALCULATOR!!!******")

    #prevent invalid inputs other than integers
    try:
        n1 = int(input("Enter the first number : "))
        n2 = int(input("Enter the second number : "))
    except ValueError:
        print("Please enter valid numbers!")
        continue
    operation = input("Enter the operation(+,-,*,**,/,//,%) : ")

    #code for arithmetic operations
    if operation == '+':
        print("Result for addition :", n1 + n2)

    elif operation == '-':
        print("Result for subtraction :", n1 - n2)

    elif operation == '*':
        print("Result for multiplication :", n1 * n2)

    elif operation == '**':
        print("Result for power :", n1 ** n2)
    elif operation == '%':
            print("Result for modulo :", n1 % n2)

    elif operation in ('/', '//'):

        # prevent division by zero
        if n2 == 0:                              
            print("Division by zero error!!")
        elif operation == '/':
            print("Result for true division : ",n1/n2)
        elif operation == '//':
            print("Result for floor division is : ",n1//n2)       
          

    else:
        print("Please enter a valid operator.") 

    #Remove spaces and make input lowercase
    answer = input("Do you want any other calculation? Type Yes/No: ").strip().lower()

    # Exit if the user types anything other than "yes"
    if answer != "yes":
        print("Thank you for using the calculator!")
        break