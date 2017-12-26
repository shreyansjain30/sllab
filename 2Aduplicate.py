def remove_dup(numbers):
    newlist=[]
    for num in numbers:
        if num not in newlist:
            newlist.append(num)
    return newlist
l=[]
n=int(input("enter the number of elements"))
for i in range(n):
    l.append(int(input()))
fl=remove_dup(l)
print(fl)