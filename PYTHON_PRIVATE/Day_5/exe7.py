# bai7
# lister=list(input())
# dictionary={}
# characters=[]
# numbers=[]
# for character in lister:
#     count=0
#     for x in  lister:
#         if x == character:
#             count+=1
#     if character not in characters:
#         dictionary[character]=count
# print(dictionary)
list_input = input()
dictionary = {}
for character in list_input:
    if character in dictionary:
        dictionary[character] += 1
    else:
        dictionary[character] = 1
print(dictionary)
