T=int(input())
Z=[]
for i in range(T):
    C=int(input())
    
    Z.append("HOT" if C>20 else "COLD")

for i in Z:
    print(i)