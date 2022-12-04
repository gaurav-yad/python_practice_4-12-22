#program to print unique elemetnts of a list
def uniqueL(L):
    Luni=[]
    for i in L:
        count_i=L.count(i)
        if count_i==1:
            Luni.append(i)
    return Luni

print(uniqueL([1,2,5,2,5,1,3,7,9]))

