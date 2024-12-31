t=int(input())
while t>0:
    t-=1
    x=int(input())
    bi=bin(x)
    bi_len=len(bi[2:])
    bi_po=((2**bi_len)-x)
    print(x-bi_po)
