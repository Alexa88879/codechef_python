T=int(input())
A=[]
for i in range(T):
    W,X,Y,Z=map(int,input().split())
    A.append(W+X*Z-Y*Z)
    
for i in A:
    print(i)
