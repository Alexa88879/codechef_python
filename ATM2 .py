t=int(input())
while t>0:
    
    n,k=map(int,input().split())
    a=input().split()
    string=''
    for i in range(n):
        
        if(int(a[i])<=k):
            string=string+"1"
            k=k-int(a[i])
            
        else:
            string=string+"0"
    print(string)
    
    
    
    
    
    
    
    
    
    
    t-=1
