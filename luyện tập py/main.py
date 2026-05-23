#bai1
def is_even(n):
    if n % 2 == 0:
     return True
    else:
        return False
print(is_even(9))
#bai2
a=int(input("nhập số thứ nhất"))
b= int(input("nhập số thứ 2"))
c = int(input("nhập sóo thứ 3 "))
if a>b and b >c:
    print("a là số lớn nhất")
elif a<b and b >c:
    print("b là số lớn nhất")
else :
    print("c là số lớn nhất")
#bai3
def greet(name="student"):
    print("Hello ", name)
greet()
greet("tham")
#bai4
a = int(input("nhập số tuổi"))
if a >1 and a<120 :
    print("bạn không đủ tuổi để truy cập web")
else :
    print("bạn đủ tuổi để truy cập web")
#bai5
string = input("Nhập 1 chuỗi bất kỳ ")
xuat_hien = string.count("a")
print("số lần xuất hiện a là:", xuat_hien)
#bai6
C = float(input("Nhập nhiệt độ: "))
F = C * 9/5 + 32
print(C,"độ C=",F,"độ F")
#bai7
weight = float(input("Nhập cân nặng:"))
height = float(input("Nhập chiều cao:"))
BMI = weight / (height * height)
print("BMI là:", round(BMI, 2))
#bai 8
a=int(input("Nhập số thứ nhất:"))
b=int(input("Nhập số thứ hai:"))
thuong = a/b
if b==0:
    print("lỗi phép tính")
else:
    print("thương=",thuong)
#bai9
a=float(input("nhập 1 số:"))
can = a**0.5
if a<0:
    print("phép tính lỗi")
else:
    print("căn bậc 2 là:", can)
#bai10
name = input("nhập tên bạn thứ 1:")
diem_toan = float(input("số điểm toán :"))
diem_ly = float(input("số điểm lý:"))
diem_hoa = float(input("dố điểm hóa:"))
diem_trung_binh = (diem_toan+diem_ly+diem_hoa)/3
print("Bạn", name, "có số điểm trung bình là:",diem_trung_binh)
name = input("nhập tên bạn thứ 2:")
diem_toan = float(input("số điểm toán :"))
diem_ly = float(input("số điểm lý:"))
diem_hoa = float(input("dố điểm hóa:"))
diem_trung_binh = (diem_toan+diem_ly+diem_hoa)/3
print("Bạn", name, "có số điểm trung bình là:",diem_trung_binh)
name = input("nhập tên bạn thứ 3:")
diem_toan = float(input("số điểm toán :"))
diem_ly = float(input("số điểm lý:"))
diem_hoa = float(input("dố điểm hóa:"))
diem_trung_binh = (diem_toan+diem_ly+diem_hoa)/3
print("Bạn", name, "có số điểm trung bình là:",diem_trung_binh)



