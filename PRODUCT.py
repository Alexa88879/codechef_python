import math
t=int(input())
while t>0:
    t-=1
    b,c=map(int,input().split())
    gcd_=math.gcd(b,c)
    print(c//gcd_)