a=input()
b=list(str(a))
c=0
for i in range(len(b)):
    if(int(b[i])==6):
        b[i]='9'
        c+=1
        break
if(c==1):
    print(int("".join(b)))
else:
    print(a)