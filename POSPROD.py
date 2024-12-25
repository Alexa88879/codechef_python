t=int(input())
while t>0:
    t-=1
    n=int(input())
    a=list(map(int,input().split()))
    pos_count=0
    neg_count=0
    for i in a:
        if(i>0):
            pos_count+=1
        elif(i<0):
            neg_count+=1
    pos_pair=(pos_count*(pos_count-1))//2
    neg_pair=(neg_count*(neg_count-1))//2
        
    print(pos_pair+neg_pair)
            