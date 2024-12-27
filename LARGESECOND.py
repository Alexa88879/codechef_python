t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    t -= 1
    a.sort(reverse=True)
    for i in range(n):
        if(a[i]!=a[i+1]):
            second_largest=a[i+1]
            break
    print(a[i]+second_largest)