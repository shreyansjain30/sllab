l=[]
n=int(input("enter the number of elements"))
for i in range(n):
    l.append(int(input()))
e=[x for x in l if x%2==0]
print(e)
print("\n")
print(l[::-1])