life = int(input())

while life > 0:
    money, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    life -= 1
    cost=0
    for i in range(money):
        if(a[i]>=x):
            cost+=b[i]
    print(cost)
        
        
