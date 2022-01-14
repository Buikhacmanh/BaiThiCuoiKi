name = input('Nhập tên đầy đủ: ')
#Tên đầy đủ: Bùi Khắc Mạnh
n = int(input("Nhập số nguyên dương n = "))
# n = BÙi Khắc Mạnh = 344
def soThuanNghich(n):
    str1 = str(n);     
    str2 = str1[::-1]; 
    if (str1 == str2):
        print("số vừa nhập là số thuận nghịch")
    else:
        print("số vừa nhập là số không thuận nghịch")
         
print("Tên đầy đủ của bạn là: ", name)
print("Tổng các chữ số của", n , "là", soThuanNghich(n))
