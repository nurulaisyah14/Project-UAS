import sys
total = []

print("-------------------------------")
print("------KASIR NURUL AISYAH-------")
print("-------------------------------")

def daftar_barang():
    print("| No |  Makanan/Minuman   | Harga |")
    print("-------------------------------")
    print("| 1  | Gorengan Tempe     | 1000  |")
    print("| 2  | Gorengan Jagung    | 2000  |")
    print("| 3  | Bakwan             | 1000  |")
    print("| 4  | Gorengan Tahu      | 1000  |")
    print("| 5  | Es Cappucino       | 5000  |")
    print("| 6  | Teh Poci           | 5000  |")
    print("| 7  | Ayam Geprek        | 15000 |")
    print("| 8  | Ayam Bakar         | 15000 |")
    print("| 9  | Nasi Goreng        | 10000 |")
    print("| 10 | Air Mineral        | 5000  |")

    print("-------------------------------")
    kode = int(input("Masukkan angka makanan  : "))
    if kode == 1:
        jumlah1 = int(input("Masukkan jumlah makanan : "))
        total1 = 1000 * jumlah1
        total.append(total1)
        tanya()
    elif kode == 2:
        jumlah2 = int(input("Masukkan jumlah makanan : "))
        total2 = 2000 * jumlah2
        total.append(total2)
        tanya()
    elif kode == 3:
        jumlah3 = int(input("Masukkan jumlah makanan : "))
        total3 = 1000 * jumlah3 
        total.append(total3)
        tanya()
    elif kode == 4:
        jumlah4 = int(input("Masukkan jumlah makanan : "))
        total4 = 1000 * jumlah4
        total.append(total4)
        tanya()
    elif kode == 5:
        jumlah5 = int(input("Masukkan jumlah makanan : "))
        total5 = 5000 * jumlah5   
        total.append(total5)
        tanya()
    elif kode == 6:
        jumlah6 =int(input("Masukan jumlah makanan :"))
        total6 = 5000 * jumlah6
        total.append(total6)
        tanya()
    elif kode == 7:
        jumlah7 =int(input("Masukan jumlah makanan :"))
        total7 = 15000 * jumlah7
        total.append(total7)
        tanya()
    elif kode == 8:
        jumlah8 =int(input("Masukan jumlah makanan :"))
        total8 = 15000 * jumlah8
        total.append(total8)
        tanya()
    elif kode == 9:
        jumlah9 =int(input("Masukan jumlah makanan :"))
        total9 = 10000 * jumlah9
        total.append(total9)
        tanya()
    elif kode == 10:
        jumlah10 =int(input("Masukan jumlah makanan :"))
        total10 = 5000 * jumlah10
        total.append(total10)
        tanya()
    return

def tanya():
    print("\n-------------------------------")
    tanya = input("Ingin tambah menu lainnya? [y/t] : ")
    print("-------------------------------")
    if tanya == "y":
        daftar_barang()
    elif tanya == "t":
        akhir()
    else:
        print("Pilihan yang anda masukan salah!")

def akhir():
    for harga in total:
        print("SubTotal         : ", sum(total))
        diskon = 0
        a = sum(total)
        if a > 500000:
            diskon = a * 8/100
        elif a > 300000:
            diskon = a * 5/100
        elif a > 200000:
            diskon = a * 3/100
        elif a > 100000:
            diskon = a * 1/100
        else:
            diskon = 0
        print("Potongan Harga   : ", diskon)
        totalakhir = a - diskon
        print("Total            : ", totalakhir)
        print("-------------------------------")
        bayar = int(input("Bayar            :  "))
        kembalian = bayar - totalakhir
        print("Kembalian        : ", kembalian)
        print("-------------------------------")
        print("          Terima Kasih         ")
        print("-------------------------------")
daftar_barang()
print("Terima kasih sudah belanja ")