t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    a=x//2
    print(min(a,y))
