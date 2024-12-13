t=int(input())
for _ in range(t):
    a_min,b_min,c_min,t_min,a,b,c=map(int,input().split())
    sum=a+b+c
    if(sum>=t_min)and(a_min<=a)and(b_min<=b)and(c_min<=c):
        print("YES")
                    
    else:
        print("NO")