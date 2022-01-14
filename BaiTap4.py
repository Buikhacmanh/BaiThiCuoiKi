BuiKhacManh = input('Nhập tên đầy đủ : ') #Viết liền không dấu VD Bùi Khắc Mạnh
MSV = input('Nhập mã sinh viên: ') # Nhập mã sinh viên VD 1451020152
print("Tên đầy đủ và mã sinh viên của bạn là: ", BuiKhacManh + MSV)
# In ra màn hình từ chuỗi ở câu a
def split(BuiKhacManh):
    return [char for char in BuiKhacManh]
print(split(BuiKhacManh))
#in ra chuỗi tên
print(tuple(MSV))
#in ra chuỗi MSV