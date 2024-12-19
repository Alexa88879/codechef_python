t=int(input())
while t>0:
    t-=1
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(n-1):
        if(a[i]>a[i+1]):
            temp=a[i]
            a[i]=a[i+1]
            a[i+1]=temp
            break
        
    if(a==sorted(a)):
        print("yes")
    else:
        print("no")