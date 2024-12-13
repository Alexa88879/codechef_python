T=int(input())
A=[]
for i in range(T):
    N,M=map(int,input().split())
    A.append("YES" if N<=(M*6*6) else "NO")
    
    
for i in A:
    print(i)
