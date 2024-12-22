t=int(input())
while t>0:
    t-=1
    gre=0
    n,k=map(int,input().split())
    g=list(map(int,input().split()))
    for i in range(n-k+1):
        l=[]
        for j in range(i,k+i):
            l.append(g[j])
        sum=0
        for m in l:
            sum=sum+m
        gre=max(sum,gre)
    print(gre)