life=int(input())
for problem in range(life):
    money=int(input())
    binary_string = input()
    str_0=binary_string.count("0")
    str_1=binary_string.count("1")
    if(str_1%2)==0 or (str_0%2)==0:
        print("yes")
    else:
        print("no")