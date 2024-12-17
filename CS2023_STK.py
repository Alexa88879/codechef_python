t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    gr_om=0
    gr_addy=0
    new_om=0
    new_addy=0
    
    for i in range(n):
        
        if(a[i]>0):
            new_om+=1
        else:
            new_om=0

        
        if (b[i]>0):
            new_addy+=1
        else:
            new_addy=0
        
        gr_om=max(gr_om,new_om)
        gr_addy=max(gr_addy,new_addy)
 
            
    if(gr_om>gr_addy):
        print("OM")
    elif(gr_addy>gr_om):
        print("ADDY")
    else:
        print("DRAW")
    t -= 1

