import math
def shorten(t, m):
    '''hàm tìm ucln rồi rút gọn'''
    x=math.gcd(t,m)
    return t/x,m/x
def multiple():
    n=int(input())
    t=1
    m=1
    for _ in range(n):
        a,b=map(int,input().split())
        t*=a
        m*=b
    t,m=shorten(t,m)
    return t,m
t,m=multiple()
print("ket qua",t,m)
