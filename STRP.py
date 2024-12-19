t=int(input())
while t>0:
    t-=1
    n=int(input())
    s=input()
    time=0
    i=0
    while i<n:
        if(i!=(n-1)):
            if(s[i]==s[i+1]):
                time+=1
                i+=1
            else:
                time+=1
        else:
            time+=1
        i+=1
    print(time)