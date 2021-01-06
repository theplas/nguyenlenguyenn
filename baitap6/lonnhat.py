import random
i = int(input())
print("nhap n",i)
danh_sach = []
for n in range(i):
    danh_sach.append(40*random.random())
    print('%d,'% danh_sach[n], end='')
vitri = 0
latd = danh_sach[vitri]
for n in range(i):
    if danh_sach[n] > latd:
        latd = danh_sach[n]
        vitri = n
print('')
print('so lon nhat la',latd)
#print('vi tri so thuc la',vitri)