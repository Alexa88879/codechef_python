t=int(input())
for _ in range(t):
    x,y,p,q=map(int,input().split())
    p1=x+p*10
    p2=y+q*10
    if(p1<p2):
        print("CHEF")
        
    elif(p2<p1):
        print("CHEFINA")
        
    else:
        print("DRAW")