T=int(input())
A=[]
for i in range(T):
    X,Y=map(int,input().split())
    A.append(X*4+Y)
    
for i in A:
    print(i)