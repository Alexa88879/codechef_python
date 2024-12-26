test=int(input())

for marks in range(test):
    a=list(map(int,input().split()))
    count_sunny=a.count(1)
    count_rainy=a.count(0)
    if(count_sunny>count_rainy):
        print("yes")
    else:
        print("no")