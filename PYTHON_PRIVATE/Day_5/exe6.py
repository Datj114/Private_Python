# bai6
dictionary_students = {
    "2022604721": 1.3,
    "2022604722": 2.5,
    "2022604723": 3.5,
    "2022604724": 4,
}
scores = sum(1 for score in dictionary_students.values() if 2.5 <= score <= 3.5)
print("so sv diem tong cao", scores)
dictionary_students["2022604725"] = 3.4
print(dictionary_students)
# key_delete=[]
# for key,score in dictionary_students.items():
#      if score<2:
#         key_delete.append(key)
key_delete = [key for key, score in dictionary_students.items() if score < 2]
for key in key_delete:
    dictionary_students.pop(key)
print(dictionary_students)
