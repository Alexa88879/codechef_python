t=int(input())
while t>0:
    t-=1
    n=int(input())
    a=input()
    b=input()
    a_set=set(b)
    no_change=0
    for i in a_set:
        if(i in a):
            str_count=b.count(i)
            count=0
            for j in range(n):
                if(i==a[j])and(i==b[j]):
                    count+=1
                    
            if(count>=str_count):
                no_change+=1
    print(len(a_set)-no_change)
            
            
                
                
    