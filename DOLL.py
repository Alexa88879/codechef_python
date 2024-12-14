t=int(input())
while t>0:
    
    n,k=map(int,input().split())
    p=input().split()
    shot=0
    for i in range(n):
        if(int(p[i])>k):
            shot+=1
    print(shot)
    
    t-=1
