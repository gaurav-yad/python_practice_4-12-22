#program to print even numbers in a list
n=int(input("Enter number of elements you want in your list: "))
l=[]
for i in range(n):
    el=int(input("Enter element :"))
    l.append(el)
l1=[]
for c in l:
    if c%2==0:
        l1.append(c)
print(l1)


