t=int(input())
while t>0:
    t-=1
    string=input()
    holes=0
    two_holes,one_holes="B","DAPORQ"
    for i in string:
        if(i in two_holes):
            holes+=2
        elif(i in one_holes):
            holes+=1
    print(holes)
    
