test = int(input())
for _ in range(test):
    n=int(input())
    a=list(map(int,input().split()))
    odd_count=0
    for i in range(n):
        if(a[i]%2)!=0:
            odd_count+=1
    
    if((odd_count%2)==0)and odd_count>0:
        print("yes")
        

    else:
        print("no")