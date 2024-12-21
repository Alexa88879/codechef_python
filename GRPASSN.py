t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    
    freq = {}
    for i in a:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    
    for group_size, count in freq.items():
        if count % group_size != 0:
            print("NO")
            break
    else:
        print("YES")
