#program to print sum of all numbers of a list
n=int(input("Enter the number of elements you want in your list: "))
l=[]
for c in range(n):
    element=int(input("Enter the element: "))
    l.append(element)

sum=0
for i in l:
    sum=sum+i
print(sum)



