import numpy as np

data = []

n = int(input("Jumlah barang: "))

for i in range(n):
    nama = input("Nama barang: ")
    kode = input("Kode barang: ")
    jumlah = int(input("Jumlah: "))
    harga = float(input("Harga per unit: "))

    data.append([nama, kode, jumlah, harga])

barang = np.array(data, dtype=object)

print("\nData inventaris:")
for i in barang:
    print(i)

total = 0
for i in barang:
    total = total + (i[2] * i[3])

print("Total nilai inventaris:", total)

cari = input("\nCari nama barang / kode barang: ")

for i in barang:
    if cari == i[0] or cari == i[1]:
        print("Data:", i)