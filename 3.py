k=0;
for x1 in ('ПОЛИН'):
    for x2 in ('ПОЛИНА'):
        for x3 in ('ПОЛИНА'):
            for x4 in ('ПОЛИНА'):
                for x5 in ('ПОЛИНА'):
                    for x6 in ('ПОЛИНА'):
                        for x7 in ('ПОЛИНА'):
                            s=x1+x2+x3+x4+x5+x6+x7
                            if ((s.count('А')==1) and (s.count('П')==1)):
                                k+=1;
print(k)

                            
