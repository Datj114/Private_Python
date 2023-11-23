# bai4
a = input().split()
b = tuple(a)
print(b)
count = 0
for x in b:
    if x.isdigit():
        count += 1
print(count)
