def c_f(t):
    return t*9/5+32
def f_c(t):
    return (t-32)*5/9

cf=[]
fc=[]
fl = True
while(fl):
    ch = int(input('Enter 1. C to F   2. F to C   3. View   4.Exit'))
    if ch == 4:
        fl = 0
    elif ch == 1 or ch == 2:
        t = float(input('Enter the temperature'))
        if ch == 1:
            tn = c_f(t)
            print (t, "C  -> ",tn, "F")
            cf.append((t, tn))
        if ch == 2:
            tn = f_c(t)
            print (t, "F  -> ",tn, "C")
            fc.append((t, tn))
    elif ch == 3:
        i = int(input('Enter 1 to sort by input or 2 to sort by output'))
        if i == 1:
            print(sorted(cf, key=lambda x:x[0]))
            print(sorted(fc, key=lambda x:x[0]))
        elif i == 2:
            print(sorted(cf, key=lambda x:x[1]))
            print(sorted(fc, key=lambda x:x[1]))
        else:
            print ('Not recognised')
    else: 
        print ('Not recognised')