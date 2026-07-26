def reverse_string(str):
    result=" "
    for ch in str:
        result=ch+result
    return result
word=input("Enter a string : ")
print("Reversed string : ",reverse_string(word))