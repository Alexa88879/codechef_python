T=int(input())
Y=[]
for i in range(T):
    N,X=map(int,input().split())
    Y.append('YES' if (X>=N/2) else "NO")
    
for i in Y:
    print(i)
    