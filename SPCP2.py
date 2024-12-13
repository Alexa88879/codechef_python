t=int(input())
for _ in range(t):
    x,n=map(int,input().split())
    
    if(n/100)>x:
        if(n%100)==0:
            p=(n//100)-x
            print(p)
        else:
            p=((n//100)+1)-x
            print(p)
            
    else:
        print(0)