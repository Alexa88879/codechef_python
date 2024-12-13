T=int(input())
A=[]
for i in range(T):
    N=int(input())
    A.append((N*1000)//100)
    
for i in A:
    print(i)
