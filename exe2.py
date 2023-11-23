# bai2
n = int(input())
a = set(map(int, input().split()))
while len(a) != n:
    a = set(map(int, input("yêu cầu nhập lại").split()))
b = int(input())
sorted(a, reverse=True)
setc = set()
for x in a:
    if sum(setc) + x <= b:
        setc.add(x)
print(setc)
