import numpy as np

data = []

n = int(input("Masukkan jumlah barang: "))

for i in range(n):
    print("\nData Barang ke-", i+1)

    nama = input("Nama Barang : ")
    kode = input("Kode Barang : ")
    jumlah = int(input("Jumlah : "))
    harga = float(input("Harga Per Unit : "))

    data.append([nama, kode, jumlah, harga])

data = np.array(data, dtype=object)

print("\n=== Data Inventaris ===")
total_inventaris = 0

for d in data:
    total = int(d[2]) * float(d[3])
    total_inventaris += total

    print("Nama:", d[0],
          "| Kode:", d[1],
          "| Jumlah:", d[2],
          "| Harga:", d[3],
          "| Total:", total)

print("\nTotal Nilai Inventaris:", total_inventaris)


# SEARCHING
cari = input("\nMasukkan Kode Barang atau Nama Barang yang dicari: ")

ditemukan = False

for d in data:
    if cari == d[0] or cari == d[1]:
        print("\nData ditemukan:")
        print("Nama Barang:", d[0])
        print("Kode Barang:", d[1])
        print("Jumlah:", d[2])
        print("Harga:", d[3])
        print("Total:", int(d[2]) * float(d[3]))
        ditemukan = True

if not ditemukan:
    print("Data tidak ditemukan")