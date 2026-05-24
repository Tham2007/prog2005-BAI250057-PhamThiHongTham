#bai1
def is_even(n):
 if n % 2 == 0 :
     return True
 else :
     return False
print(is_even(9))
#bai2
a=int(input("nhấp số thứ nhất:"))
b=int(input("nhấp số thứ hai:"))
c=int(input("nhập số thứ ba:"))
if a>b and b>c:
    print("số thứ nhất lớn nhất")
elif a<b and c<b :
    print("số thứ hai lớn nhất")
else:
    print("số thứ 3 lớn nhất")
#bai3
def greet(name="student"):
    print("hello",name)
greet()
greet("heidi")
#bai4
a=int(input("Nhập số tuổi của bạn:"))
if a >1 and a<120:
    print("Độ tuổi của bạn phù hợp")
else:
    print("độ tuổi của bạn không phù hợp")
#bai5
string = input("nhập chuỗi bất kỳ:")
so_lan = string.count("a")
print("số lần xuất hiện ký tự a là:",so_lan)
#bai6
C=float(input("Nhập độ C hiện tại"))
F=C*9/5+32
print(C,"độ C=",F,"độ F")
#bai7
weight=float(input("nhập cân nặng của bạn(kg)"))
height=float(input("nhập chiều cao của bạn(m)"))
BMI=weight/(height*height)
print("BMI=",round(BMI,2))
#bai8
a=int(input("nhập số thứ 1"))
b=int(input("nhập số thứ hai"))
if b!=0:
    thuong=a/b
    print(thuong)
else:
    print("lỗi")
#bai9
a=float(input("nhập số bất kỳ"))
can=a**0.5
if a<0:
    print("phép tính lỗi")
else:
    print(can)
#bai10
name = input("nhập tên bạn thứ 1:")
diem_toan = float(input("số điểm toán :"))
diem_ly = float(input("số điểm lý:"))
diem_hoa = float(input("số điểm hóa:"))
diem_trung_binh = (diem_toan+diem_ly+diem_hoa)/3
print("Bạn", name, "có số điểm trung bình là:",diem_trung_binh)
name = input("nhập tên bạn thứ 2:")
diem_toan = float(input("số điểm toán :"))
diem_ly = float(input("số điểm lý:"))
diem_hoa = float(input("số điểm hóa:"))
diem_trung_binh = (diem_toan+diem_ly+diem_hoa)/3
print("Bạn", name, "có số điểm trung bình là:",diem_trung_binh)
name = input("nhập tên bạn thứ 3:")
diem_toan = float(input("số điểm toán :"))
diem_ly = float(input("số điểm lý:"))
diem_hoa = float(input("số điểm hóa:"))
diem_trung_binh = (diem_toan+diem_ly+diem_hoa)/3
print("Bạn", name, "có số điểm trung bình là:",diem_trung_binh)





