t=int(input())
while t>0:
    t-=1
    n,k = map(int,input().split())
    d = list(map(int,input().split()))
    string=''
    for i in d:
        if(i%k)==0:
            string+="1"
        else:
            string+="0"
    print(string)
    