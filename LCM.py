x,y=map(int,input().split())
if x>y:
    big=x
else:
    big=y
while True:
    if((big%x==0)) and ((big%y==0)):
        lcm=big
        break
    big+=1
print(lcm)
        