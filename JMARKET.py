for _ in range(int(input())):
    x,a,b,c =map(int,input().split())
    lis=[a,b,c]
    lis.sort()
    least=lis[0]+lis[1]
    for _ in range(x-2):
        least=least+lis[0]
    print(least)
    
