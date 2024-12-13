T=int(input())
for i in range(T):
    X=int(input())
    if (X%3)==0:
        print(0)
    else:
        print(3-(X%3))