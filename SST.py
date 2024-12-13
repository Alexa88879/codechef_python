T=int(input())
for i in range(T):
    A,B=map(int,input().split())
    X=A*100//10
    Y=B*100//20
    if X>Y:
        print("FIRST")
    elif Y>X:
        print("SECOND")
    else:
        print("ANY")