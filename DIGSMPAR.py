t=int(input())
while t>0:
    t-=1
    n=int(input())
    digit_sum=0
    for i in str(n):
        digit_sum+=int(i)
    
    if(digit_sum%2)==0:
        while True:
            di_sum=0
            n+=1
            for i in str(n):
                di_sum+=int(i)
            if(di_sum%2)!=0:
                print(n)
                break
    else:
        while True:
            di_sum=0
            n+=1
            for i in str(n):
                di_sum+=int(i)
            if(di_sum%2)==0:
                print(n)
                break
                
            
        
    
