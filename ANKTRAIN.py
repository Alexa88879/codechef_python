t=int(input())
for _ in range(t):
    n=int(input())
    if(n%8)==0 or(n%8)==7:
        if(n%8)==0:
            print(f"{n-1}SL")
        else:
            print(f"{n+1}SU")
    else:
        if(n%8)==1:
            print(f"{n+3}LB")
        elif(n%8)==4:
            print(f"{n-3}LB")
        elif(n%8)==2:
            print(f"{n+3}MB")
        elif(n%8)==5:
            print(f"{n-3}MB")
        elif(n%8)==3:
            print(f"{n+3}UB")
        else:
            print(f"{n-3}UB")