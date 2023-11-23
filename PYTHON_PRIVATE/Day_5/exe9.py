# bai9
import random

n = int(input())
major = ["CNTT", "KHMT", "KTPM", "HTTT"]
while n < 10 or n >= 100000:
    n = int(input("nhap lai"))
dict_info = {}
for i in range(n):
    id_student = 2021600000 + i + 1
    password = random.choice(major) + str(id_student)
    dict_info[f"Account{i+1}"] = {"usename": str(id_student), "password": password}
# print(dict_info)
for key, value in dict_info.items():
    print(key, value)
