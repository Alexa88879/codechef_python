import math
t=int(input())
for _ in range(t):
    x,y,z=map(int,input().split())
    # a=math.ceil(y/z)
    # print(x*a)
    if(y%z)==0:
        print((y//z)*x)
        
    else:
        a=(y//z)+1
        print(a*x)