t=int(input())
while t>0:
    r1,w1,c1=map(int,input().split())
    r2,w2,c2=map(int,input().split())
    r=max(r1,r2)
    w=max(w1,w2)
    c=max(c1,c2)
    a=0
    b=0
    if(r==r1):
        a+=1
    else:
        b+=1
        
    if(w==w1):
        a+=1
    else:
        b+=1
        
    if(c==c1):
        a+=1
    else:
        b+=1
        
    if(a>b):
        print("A")
        
    else:
        print("B")
    t-=1
    
