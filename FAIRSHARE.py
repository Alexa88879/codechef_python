t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    if n>k:
        if (n%(k+1))==0:
            
            print(n//(k+1))
            
        else:
            p=n//(k+1)
            q=n-p*(k+1)
            print(p+q)
            
    else:
        print(n)