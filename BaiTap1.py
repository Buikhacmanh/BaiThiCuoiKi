Manh = input("Nhập vào tên: ")
#Tên: Mạnh
print("Tên của bạn là: ", Manh)
dodai = len(str(Manh))
# độ dài của tên (ex: Mạnh = 4)
print("Độ dài tên n = ", dodai)
j = dict()
for i in range(1, dodai + 1):
    j[i] = i * i
print("Dictionary độ dài của tên là:  ", j)