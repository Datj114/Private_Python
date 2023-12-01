def SumIndex():
    ''' function tính tổng số từ đầu đến i'''
    n=int (input())
    a=list(map(int,input().split()))
    t=int(input())
    for _ in range(t):
        i=int(input())
        result=0
        for x in range(i+1):
            result +=a[x]
            print(result) 
SumIndex()
