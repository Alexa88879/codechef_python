T=int(input())
for i in range(T):
    pa,pb,qa,qb=map(int,input().split())
    p=max(pa,pb)
    q=max(qa,qb)
    if(p>q):
        print("Q")
    elif(q>p):
        print("P")
    else:
        print("TIE")
