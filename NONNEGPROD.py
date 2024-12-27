test=int(input())
for _ in range(test):
    n=int(input())
    a=list(map(int,input().split()))
    if 0 in a:
        print(0)
    else:
        a.sort()
        count=0
        for i in range(n):
            if(a[i]<0):
                count+=1
            else:
                break
        if(count%2)==0:
            print(0)
        else:
            print(1)