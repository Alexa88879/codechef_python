for _ in range(int(input())):
    p,m,v=map(int,input().split())
    total=m*v
    maximum=total-v*(p-1)
    print(maximum)