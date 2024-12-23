t=int(input())
while t>0:
    t-=1
    s=input()
    sum=0
    for i in s:
        try:
            sum=sum+int(i)
            
        except:
            continue
    print(sum)