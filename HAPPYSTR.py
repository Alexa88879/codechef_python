t = int(input())

while t > 0:
    s = input()
    vowel=['a','e','i','o','u']
    flag=0
    for i in range(len(s)-2):
            if(s[i] in vowel)and(s[i+1] in vowel)and (s[i+2] in vowel):
                print("HAPPY")
                flag=1
                break
    if(flag==0):
        print("SAD")
    t -= 1
