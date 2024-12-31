t=int(input())
while t>0:
    t-=1
    n=int(input())
    a=list(map(int,input().split()))
    even_cont=0
    for i in a:
        if(i%2)==0:
            even_cont+=1
        
    if(even_cont==len(a)):
        print(0)
    else:
        
        print(even_cont)