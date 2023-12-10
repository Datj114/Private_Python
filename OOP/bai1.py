class Pycon():
    id_count=0
    total_age=0
    def __init__(self):
        Pycon.id_count+=1
        self.id=Pycon.id_count
        self.fullName=''
        self.age=0
    def inputInfor(self):
        self.fullName=input("nhap ten ")
        self.age=int(input())
        Pycon.total_age+=self.age
    @classmethod
    def averAge(self,n):
        return Pycon.total_age/n
    
    def __str__(self) -> str:
        return f"Id: {self.id} || Tên: {self.fullName} || Tuổi: {self.age}"
# Nhập số lượng Pycon
n = int(input())

pycons = []

# Nhập thông tin và in ra thông tin của từng Pycon
for _ in range(n):
    pycon = Pycon()
    pycon.inputInfor()
    pycons.append(pycon)
    print(pycon)

# In trung bình độ tuổi của các Pycon
print(f"Trung bình tuổi: {Pycon.averAge(n)}")

