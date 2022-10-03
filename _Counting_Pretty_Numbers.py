t=int(input())
for i in range(t):
    L,R=map(int,input().split())
    count=0
    for i in range(L,R+1):
        if i%10==2 or i%10==3 or i%10==9:
            count+=1
    print(count)