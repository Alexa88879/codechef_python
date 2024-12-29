test=int(input())
while test>0:
    test-=1
    n,x = map(int,input().split())
    a=list(map(int,input().split()))
    max_people=x
    add_people=x
    for i in a:
        if(i>=0):
            add_people=add_people+i

        else:
            add_people=add_people+i
        
        max_people=max(add_people,max_people)
    print(max_people)