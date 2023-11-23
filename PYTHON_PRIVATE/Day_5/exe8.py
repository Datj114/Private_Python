# bai8
championLOL = [" Yasuo", " Lee Sin", " Zed", " Master Yi", " Garen", " Tryndamere"]
dataLOL = [
    {" price": 6300, " Ulti": " Trăn trối"},
    {" price": 4800, " Ulti": " Nộ Long Cước"},
    {" price": 4800, " Ulti": " Dấu Ấn Tử Thần"},
    {" price": 450, " Ulti": " Chiến Binh Sơn Cước"},
    {" price": 450, " Ulti": " Công Lý Demacia"},
    {" price": 1350, " Ulti": " Từ Chối Tử Thần"},
]
# mydict={}
# for champion,price in zip(championLOL,dataLOL):
#     mydict[champion]=price
mydict = {champion: price for champion, price in zip(championLOL, dataLOL)}
print(mydict)
s = input()
if s in mydict:
    print(mydict[s])
