# bai5
s = set(map(int, input().split()))
if 11 not in s:
    s.add(int(11))
print(s)
a = list(s)
b = []
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] + a[j] == 11:
            b.append((a[i], a[j]))
b = tuple(b)
print(sum(sum(x) for x in b))
