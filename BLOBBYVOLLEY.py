t = int(input())

while t > 0:
    n = int(input())
    s = input()
    a_s , a_r , b_s , b_r = [1,0,0,1]
    alice_score=0
    bob_score=0
    for i in range(n):
        if(a_s==1)and(s[i]=='A'):
            alice_score += 1
        elif(a_s==1)and(s[i]=="B"):
            a_s=0
            a_r=1
            b_s=1
            b_r=0
        elif(b_s==1)and(s[i]=="B"):
            bob_score += 1
        elif(b_s==1)and(s[i]=="A"):
            a_s=1
            a_r=0
            b_s=0
            b_r=1
    print(alice_score,bob_score)
    t -= 1
