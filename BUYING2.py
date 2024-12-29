t=int(input())
while t>0:
    t-=1
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    total_notes=sum(a)
    flag=True
    if(total_notes%x)!=0:
        rem=total_notes%x
        for i in range(n):
            if(a[i] in range(1,rem+1)):
                flag=False
                print(-1)
                break
        if flag:
            print(total_notes//x)
            
    else:
        print(total_notes//x)