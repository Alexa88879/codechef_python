t=int(input())
while t>0:
    t-=1
    n=int(input())
    i=n
    bi_str=''
    while i!=1:
        if(i%2)==0:
            bi_str='0'+bi_str
        else:
            bi_str='1'+bi_str
        i//=2

    bi_str='1'+bi_str
    print(bi_str.count('1')-1)
# only this code can also work
#     print(bin(n).count("1")-1)