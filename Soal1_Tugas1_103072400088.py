def isKabisat(tahun):  
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    else:
        return False

print(isKabisat(int(input("Tahun: "))))