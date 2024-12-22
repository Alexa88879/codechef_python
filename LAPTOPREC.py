t=int(input())
while t>0:
    t-=1
    n=int(input())
    a=list(map(int,input().split()))
    count_dict={}
    for i in range(1,11):
        coun=a.count(i)
        count_dict[i]=coun
        
    cou_list = sorted(count_dict.values(),reverse=True)
    if(cou_list[0]==cou_list[1]):
        print("confused")
    else:
        for i in range(1,11):
            if(count_dict[i]==cou_list[0]):
                print(i)