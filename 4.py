from itertools import *
for y in product ('12', repeat = 46):
    s=''.join(y)
    s='0'+s+'0'
    while (not '00' in s):
        s=s.replace('011','20')
        s=s.replace('022','10')
        s=s.replace('01','220')
        s=s.replace('02','110')
        if ((s.count('1')==40) and (s.count('2')>50)):
            print(s)
