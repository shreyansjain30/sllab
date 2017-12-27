import os
import sys
with open(sys.argv[1]) as fh:
	s = fh.read().split()

dict = {}
for i in s:
	if i in dict.keys():
		dict[i] = dict[i] + 1
	else:
		dict[i] = 1
ls = sorted(dict.items(),key=lambda t:t[1],reverse=True)
ls = ls[:11]
print (ls)
lst = []
for i in ls:
	lst.append(len(i[0]))
print(lst)
def avg(lst):
	return(sum(lst)/len(lst))
print(avg(lst))
odd = [i*i for i in lst if i%2==1]
print(odd)