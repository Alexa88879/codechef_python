t=int(input())
while t>0:
    t-=1
    n=int(input())
    s=input()
    vow=['a','i','e','o','u']
    flag=True
    for i in range(n-3):
        count=0
        for j in range(i,i+4):
            if(s[j] not in vow):
                count+=1
        if(count==4):
            flag=False
            print("no")
            break
    if(flag):
        print("yes")
            
        
    
