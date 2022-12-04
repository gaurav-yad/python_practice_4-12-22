#program to reverse a string
str1=input("Enter the string: ")
for i in range(-1,-len(str1)-1,-1):
    print(str1[i],end="")