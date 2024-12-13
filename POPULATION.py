T=int(input())
A=[]

for i in range(T):
    X,Y,Z=map(int,input().split())
    A.append(X+Z-Y)
    
for i in A:
    print(i)
    