t=int(input())
while t>0:
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    
    for i in range(n):
        if(i!=(n-1)):
            if(a[i]>=k):
                rem=a[i]-k
                a[i+1]=a[i+1]+rem
                
            else:
                print("No",i+1)
                break
        else:
           if(a[i]>=k):
               print("yes")
                
           else:
                print("No",i+1)

    t-=1
