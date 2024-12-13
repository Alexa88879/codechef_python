t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    p=input().split()
    
    total_revenue=0
    for i in p:
        total_revenue=total_revenue+int(i)
        
    for i in range(n):
        if(int(p[i])>k):
            p[i]=k
    revenue=0
    for i in p:
        revenue=revenue+int(i)
        
    print(total_revenue-revenue)