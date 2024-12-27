test=int(input())
for _ in range(test):
    a=list(map(int,input().split()))
    team1=0
    team2=0
    for i in range(10):
        if(i%2)==0 and (a[i]==1):
            team1+=1
        else:
            if(a[i]==1):
                team2+=1
    if(team1>team2):
        print(1)
    elif(team2>team1):
        print(2)
    else:
        print(0)
        
