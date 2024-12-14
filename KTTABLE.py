t=int(input())
while t>0:
    n=int(input())
    A=input().split()
    B=input().split()
    st_cook=0
    for i in range(n):
        if(i==0)and(int(A[0])>=int(B[0])):
            st_cook += 1
            
        else:
            time_given=int(A[i])-int(A[i-1])
            if(time_given>=int(B[i])):
                st_cook += 1
        
    print(st_cook)
            
    
    
    t-=1