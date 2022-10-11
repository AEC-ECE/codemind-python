t=int(input())
for i in range(t):
    n=int(input())
    next_prime=n
    while True:
        fc=0
        for j in range (1,next_prime+1):
            if next_prime%j==0:
                fc+=1
        if fc==2:
            break
        next_prime+=1
       
    p_prime=n
    while True:
        fc=0
        for s in range(1,p_prime+1):
            if p_prime%s==0:
                fc+=1
        if fc==2:
            break
        p_prime-=1
        
    if n-p_prime<=next_prime-n:
        print(p_prime)
    else:
        print(next_prime)