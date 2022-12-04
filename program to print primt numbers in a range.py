#program to print primt numbers in a range
strt=int(input("Enter starting  of range: "))
end=int(input("Enter ending of range: "))
for i in range(strt,end+1):
    for c in range(2,i):
        if i%c==0:
            break
    else:
        print(i,end=",")
print("These are the prime numbers in the range")

    
