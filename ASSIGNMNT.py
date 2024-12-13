T=int(input())
A=[]
for i in range(T):
    X,Y,Z=map(int,input().split())
    A.append("YES" if ((X*Y)<=(Z*60*24)) else "NO")
        
for i in A:
    print(i)