t=int(input())
while t>0:
    t-=1
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    fru_dict={}
    for i in range(n):
        fru_type=a[i]
        nutrition=b[i]
        if fru_type not in fru_dict.keys():
            fru_dict[fru_type]=nutrition
        else:
            if(nutrition>fru_dict[fru_type]):
                fru_dict[fru_type]=nutrition
    max_nutri=0
    for val in fru_dict.values():
        if(val>0):
            max_nutri=max_nutri+val
    print(max_nutri)