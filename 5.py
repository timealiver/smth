f = open('hh.txt').readline()
k = 0
kmax=0
i=1
while (i<=len(f)-2):
    if ((f[i] in 'CDF') and (f[i+1] in 'CDF') and (f[i+2] in 'AO')):
        i+=3
        k+=3
        kmax=max(k,kmax)
    else:
        k=0
        i+=1
print(i,kmax)
