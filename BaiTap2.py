Khac = input('Nhập tên đệm của bạn: ')
#Tên đệm: Khắc
def sum(n):
    manh = 0
    while (n > 0):
        manh = manh + n % 10
        n = int(n / 10)
    return manh
 
n = int(input("Nhập số nguyên dương( là tên + tên đệm của bạn) n = "));#Họ tên đệm: Khắc Mạnh ex: 44
print("Tên đệm của bạn là: ", Khac)
print("Tổng các chữ số của", n , "là", sum(n));