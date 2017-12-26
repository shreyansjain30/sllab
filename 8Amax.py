def findmax(l):
    if(len(l)==1):
        return l[0]
    else:
        rem=l[1:]
        if(l[0]>findmax(rem)):
            return l[0]
        else:
            return findmax(rem)
l=[]
n=int(input("enter the number of elements "))
for i in range(n):
    l.append(int(input()))
m=findmax(l)
print(m)