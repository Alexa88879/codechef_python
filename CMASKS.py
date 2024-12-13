T=int(input())
Z=[]
for i in range(T):
    X,Y=map(int,input().split())
    Z.append("CLOTH" if ((X*100)>=(Y*10)) else "DISPOSABLE")
    
for i in Z:
    print(i)
