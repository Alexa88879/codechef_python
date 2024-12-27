test=int(input())
for _ in range(test):
    a,b,c,d=map(int,input().split())
    integer=[]
    
    for i in range(a,b+1):
        if(i not in integer):
            integer.append(i)
    
    for i in range(c,d+1):
        if(i not in integer):
            integer.append(i)
    print(len(integer))