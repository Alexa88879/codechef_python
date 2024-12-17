t=int(input())
while t>0:
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    flag=0
    for i in range(2*n-2):
        if(a[i]==a[i+1])and (a[i+1]==a[i+2]):
            flag=1
            break
        
        
    if(flag==0):
        print("yes")
    else:
        print("no")
    
    
    t-=1