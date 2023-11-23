# bai3
T = input()
a = T.split()
max = 0
for i in a:
    x = a.count(i)
    if x > max:
        max = x
b = []
for i in a:
    if max == a.count(i) and (i, max) not in b:
        b.append((i, max))
c = tuple(b)
print(c)
