t=int(input())
while t>0:
    t-=1
    n=int(input())
    a=list(map(int,input().split()))
    ani_dict={}
    if(n%2)!=0:
        print("no")
    else:
        for i in range(n):
            b=a[i]
            if b not in ani_dict.keys():
                ani_dict[b]=1
            else:
                for j in ani_dict.keys():
                    if(j==b):
                        ani_dict[b]+=1
        for k in ani_dict.values():
            if(k%2)!=0:
                print("no")
                break
        else:
            print("yes")