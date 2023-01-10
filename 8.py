from random import choice
x=int(input())
a=[]
for i in range(1,x+1):
    x1=choice(['А', 'В', 'Е', 'К', 'М', 'Н', 'О', 'Р', 'С', 'Т', 'У', 'Х'])
    x2=choice(['0','1','2','3','4','5','6','7','8','9'])
    x3=choice(['0','1','2','3','4','5','6','7','8','9'])
    x4=choice(['0','1','2','3','4','5','6','7','8','9'])
    x5=choice(['А', 'В', 'Е', 'К', 'М', 'Н', 'О', 'Р', 'С', 'Т', 'У', 'Х'])
    x6=choice(['А', 'В', 'Е', 'К', 'М', 'Н', 'О', 'Р', 'С', 'Т', 'У', 'Х'])
    s=x1+x2+x3+x4+x5+x6
    a.append(s)
print(a)
length=len(str(max(a)))
rang=12
p=0
i=0
figure=0
for i in range (length):
    B=[[] for k in range(rang)]
    for p in a:
        figure=((p/10)**i )%10
        B[figure].append(p)
    a=[]
    for k in range(rang):
        a=a+B[k]
print(a)

