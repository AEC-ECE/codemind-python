from math import sqrt
a,b,c=map(int,input().split())
area=(sqrt((4*(a**2)*(b**2))-((a**2+b**2-c**2)**2)))/4
print('{:.2f}'.format(area))