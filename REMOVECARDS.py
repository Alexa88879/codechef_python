t=int(input())
while t>0:
    t-=1
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    count=1
    maxi=1
    for i in range(n-1):
        if(a[i]==a[i+1]):
            count+=1
        else:
            count=1
        maxi=max(maxi,count)
    print(n-maxi)
        
