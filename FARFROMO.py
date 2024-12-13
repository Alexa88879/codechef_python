import math
t=int(input())
for _ in range(t):
    x1,y1,x2,y2=map(float,input().split())
    da=(x1**2)+(y1**2)
    db=(x2**2)+(y2**2)
    
    if (da**2)>(db**2):
        print("ALEX")
        
    elif(db**2)>(da**2):
        print("BOB")
        
    else:
        print("EQUAL")