goals=int(input())
while goals>0:
    goals-=1
    n=int(input())
    a=list(map(int,input().split()))
    max_peo=set()
    max_no=0
    for i in a:
        if i not in max_peo:
            max_peo.add(i)
            max_no=max(max_no,len(max_peo))
            
        else:
            max_no=max(max_no,len(max_peo))
            max_peo.remove(i)
    print(max_no)