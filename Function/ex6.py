x = [50, 75, 80, 60, 70, 90, 100, 65, 85, 105]
y = [600, 860, 930, 700, 800, 1040, 1150, 750, 970, 1200]
n = len(x)
w = 0
b = 0
while Loss**0.5 < 0.001:
    c = [w * x[i] + b for i in range(n)]
    Loss = 1 / (2 * n) * sum(((c[i] - y[i]) ** 2) for i in range(n))
    w += 0.0001
    b += 0.0001
print("gia tien dien tich 40", w * 40 + b)
