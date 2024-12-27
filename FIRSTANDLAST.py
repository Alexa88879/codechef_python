test=int(input())
for _ in range(test):
    n=int(input())
    a=list(map(int,input().split()))
    first=a[0]
    last=a[n-1]
    sum_list=[first+last]
    for i in range(n):
        poped=a.pop()
        a.insert(0,poped)
        s=a[0]+a[n-1]
        sum_list.append(s)
        
    sum_list.sort(reverse=True)
    print(sum_list[0])
    
        
