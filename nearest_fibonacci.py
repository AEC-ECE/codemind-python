a=int(input())
b=0
c=1
d=0
while (d<=a):
    f=d
    d=b+c
    b=c
    c=d
    e=d
g=abs(a-f)
h=abs(a-e)
if (g==h):
    print(min(e,f),max(e,f))
elif (g>h):
    print(e)
else:
    print(f)
