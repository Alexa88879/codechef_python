import math
t=int(input())
for _ in range(t):
    x=int(input())
    # s=math.ceil((100)/(x*0.2))
    # print(s)
    if((100)%(x*0.2))==0:
        s=(100)//(x*0.2)
    
        print(int(s))
        
    else:
        s=(100)//(x*0.2)+1
        print(int(s))