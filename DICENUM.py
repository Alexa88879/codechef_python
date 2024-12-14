t=int(input())
while t>0:
    
    a1,a2,a3,b1,b2,b3=map(int,input().split())
    A=[a1,a2,a3]
    B=[b1,b2,b3]
    A.sort(reverse=True)
    B.sort(reverse=True)
    Alice=100*A[0]+10*A[1]+A[2]
    bob=100*B[0]+10*B[1]+B[2]
    if (Alice>bob):
        print("ALICE")
        
    elif(bob>Alice):
        print("BOB")
        
    else:
        print("TIE")
    
    
    
    
    
    
    
    
    
    
    
    
    
    t-=1
