n=int(input())
s=0
for i in range(1,n+1):
    a=((n**2)%10)
    b=((n**2)//10)
    s+=a
if(n==s):
    print("Neon Number")
else:
    print("Not Neon Number")

