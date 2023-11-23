# bai1
sv_b1 = set(map(int, input().split()))
sv_b2 = set(map(int, input().split()))
sv = sv_b1 & sv_b2
if sv:
    print("sv dang ky ca 2 la", sv)
else:
    print("ko co sv dky ca hai")
print("danh sach tong hop", sv_b1 | sv_b2)
print("sv dang ky tại bàn 1 ko dky bàn 2", sv_b1 - sv_b2)
print("sv dang ky duy nhat 1 bàn", (sv_b1 | sv_b2) - (sv_b1 & sv_b2))
