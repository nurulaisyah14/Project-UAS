# Project-UAS
## PROFIL
| Variable           |             Isi            |
| -------------------|----------------------------|
| **Nama**           |         Nurul Aisyah       |
| **NIM**            |          312310476         |
| **Kelas**          |          TI.23.A.5         |
| **Mata Kuliah**    |     Bahasa Pemrograman     |
| **Dosen Pengampu** | Agung Nugroho,S.Kom.,M.Kom |

# Tugas Project Ujian Akhir Semester

## **Program Kasir Di Sebuah Kantin**<br>

|Link Youtube|... |
| --- | --- |

# CODE PROGRAM PYTHON
![Screenshot 2024-01-09 204529](https://github.com/nurulaisyah14/Project-UAS/assets/148174512/b9471f70-b01e-4af8-87fb-8122f87607da)
![Screenshot 2024-01-09 204545](https://github.com/nurulaisyah14/Project-UAS/assets/148174512/c5441231-5ceb-4b70-9131-a6362dda22ff)
![Screenshot 2024-01-09 204559](https://github.com/nurulaisyah14/Project-UAS/assets/148174512/f4790582-c3a4-4ecf-9e54-1d4252001356)




# HASIL DARI CODE PROGRAM 
![Screenshot 2024-01-09 203317](https://github.com/nurulaisyah14/Project-UAS/assets/148174512/c7f3706e-f6fc-4909-afc0-e3db629a9904)


# $${\color{lightblue}PENJELASAN}$$
1. Kode program ini adalah definisi dari fungsi daftar_barang(). Fungsi ini bertujuan untuk menampilkan daftar makanan dan minuman beserta harganya.
```python
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

```

2. Kode program ini merupakan bagian dari fungsi yang digunakan untuk memproses pilihan makanan atau minuman yang dimasukkan oleh pengguna.
```python
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

```

3. Kode program ini merupakan definisi dari fungsi tanya(). Fungsi ini bertujuan untuk menanyakan kepada pengguna apakah mereka ingin menambahkan menu makanan atau minuman lainnya.
```python
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
```

4. Kode program ini adalah definisi dari fungsi akhir(). Fungsi ini bertujuan untuk menghitung total pembelian, memberikan diskon berdasarkan total harga, menghitung kembalian, dan menampilkan pesan terima kasih kepada pengguna.
```python
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
```
* Program yang diberikan adalah program sederhana Python yang mensimulasikan sistem kasir. Program ini terdiri dari beberapa fungsi, yaitu daftar_barang(), tanya(), dan akhir().
Fungsi daftar_barang() menampilkan daftar item dengan harga, mengambil input dari pengguna untuk kode item dan jumlahnya, dan menghitung total harga. Pertama-tama, fungsi ini menampilkan daftar item dengan harga menggunakan perintah print(). Kemudian, pengguna diminta untuk memasukkan kode item menggunakan perintah input() dan diubah menjadi integer menggunakan int(). Setelah itu, program menggunakan if-elif-else statements untuk menentukan harga item berdasarkan kode yang dimasukkan pengguna. Jumlah item juga diminta dari pengguna dan dihitung total harganya. Total harga disimpan dalam list total menggunakan perintah append(). Setelah itu, fungsi tanya() dipanggil.
* Fungsi tanya() menanyakan apakah pengguna ingin menambahkan item lain atau tidak. Jika pengguna ingin menambahkan item lain, fungsi daftar_barang() dipanggil kembali. Jika tidak, fungsi akhir() dipanggil.
* Fungsi akhir() menghitung diskon berdasarkan total harga, menghitung kembalian, dan menampilkan pesan terima kasih. Pertama-tama, fungsi ini menggunakan perintah for untuk menghitung total harga dari semua item yang dibeli menggunakan perintah sum(). Kemudian, diskon dihitung berdasarkan total harga menggunakan if-elif-else statements. Setelah itu, total harga setelah diskon dihitung dan ditampilkan menggunakan perintah print(). Pengguna diminta untuk memasukkan jumlah uang yang dibayarkan menggunakan input() dan diubah menjadi integer menggunakan int(). Kembalian dihitung dan ditampilkan menggunakan perintah print(). Terakhir, pesan terima kasih ditampilkan menggunakan print().
* Program ini menggunakan built-in Python functions seperti print(), input(), int(), sum(), dan if-elif-else statements. Program ini tidak memerlukan pustaka eksternal dan tidak menggunakan import sys.

