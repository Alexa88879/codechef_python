for _ in range(int(input())):
    n=int(input())
    p=input().split()
    sat_sun=[6,13,20,27,7,14,21,28]
    for i in range(n):
        if(int(p[i]) not in sat_sun):
            sat_sun.append(int(p[i]))
            
    print(len(sat_sun))