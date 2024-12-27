t = int(input())

while t > 0:
    n = int(input())
    d = list(map(int, input().split()))
    # Your code goes here
    t -= 1
    sor_d=sorted(d)
    if(sor_d==d):
        print("yes")
    else:
        print("no")