import math
import statistics

print(30*"=")
print("Program Klakulator")
print("1. Kalkulator Matematika")
print("2. Kalkulator Fisika")
print("3. Tentang Program")
jenis_kalkulator = int(input("Pilih kalkulator [1/2] :"))
print(30*"=")
if jenis_kalkulator == 1:
    print("1. Operasi aritmatika dasar")
    print("2. Trigonometri")
    print("3. Menghitung bunga bank")
    print("4. Mean Median Modus")
    print("5. Volume Balok")
    jenis_matematika = int(
        input("Pilih salah satu jenis matematika [1/2/3/4/5] :"))
    if jenis_matematika == 1:
        print(30*"=")
        print("Operasi aritmatika dasar")
        print(" 1. Penjumlahan  \t [+]")
        print(" 2. Pengurangan  \t [-]")
        print(" 3. Perkalian    \t [x]")
        print(" 4. Pembagian    \t [:]")
        print(30*"=")

        operasi = int(input("Pilih operasi diatas [1/2/3/4] :"))
        angka1 = float(input("Masukkan bilangan pertama :"))
        angka2 = float(input("Masukkan bilangan kedua :"))

        print(30*"=")
        if operasi == 1:
            hasil = angka1 + angka2
            print("Hasil penjumlahan dari ", angka1, "+", angka2, "=", hasil)
        elif operasi == 2:
            hasil = angka1 - angka2
            print("Hasil pengurangan dari ", angka1, "-", angka2, "=", hasil)
        elif operasi == 3:
            hasil = angka1 * angka2
            print("Hasil perkalian dari ", angka1, "x", angka2, "=", hasil)
        elif operasi == 4:
            hasil = angka1 / angka2
            print("Hasil pembagian dari ", angka1, ":", angka2, "=", hasil)
        else:
            print("Operan tidak ditemukan")

    elif jenis_matematika == 2:
        print(30*"=")
        print("Trigonometri")
        print(" 1. Sin()")
        print(" 2. Cos()")
        print(" 3. Tan()")
        print(" 4. Sec()")
        print(" 5. Cosc()")
        print(" 6. Cot()")

        trigonometri = int(input("Pilih salah satu [1/2/3] :"))
        print(30*"=")
        if trigonometri == 1:
            sin = float(input("Masukkan sudut sinus :"))
            print("Hasil dari sin(", sin, ") =", math.sin(sin))
        elif trigonometri == 2:
            cos = float(input("Masukkan sudut cosinus :"))
            print("Hasil dari cos(", cos, ") =", math.cos(cos))
        elif trigonometri == 3:
            tan = float(input("Masukkan sudut tangen :"))
            print("Hasil dari tan(", tan, ") =", math.tan(tan))
        elif trigonometri == 4:
            sec = float(input("Masukkan sudut secan :"))
            print("Hasil dari secan(", sec, ") =", 1/math.cos(sec))
        elif trigonometri == 5:
            cosc = float(input("Masukkan sudut cosecan :"))
            print("Hasil dari cosecan(", cosc, ") =", 1/math.sin(cosc))
        elif trigonometri == 6:
            cot = float(input("Masukkan sudut cotangen :"))
            print("Hasil dari cotangen(", cot, ") =", 1/math.tan(cot))
        else:
            print("Data tidak valid")

    elif jenis_matematika == 3:
        print(30*"=")
        print("Menghitung Bunga Bank")
        tahun = int(input("Masukkan banyak tahun :"))
        tabungan_awal = int(input("Masukkan jumlah tabungan awal :"))
        print(30*"=")
        for i in range(1, tahun+1):
            tabungan_awal = tabungan_awal + (tabungan_awal * 0.1)
            print("Tahun ke =>", i)
            print(f"Saldo anda sekarang = Rp.{tabungan_awal:,}")
            print(30*"=")

    elif jenis_matematika == 4:
        print(30*"=")
        print("Mencari Mean Median Modus")
        print(" 1. Mean")
        print(" 2. Median")
        print(" 3. Modus")

        mmm = int(input("Pilih salah satu [1/2/3] :"))
        print(30*"=")
        if mmm == 1:
            data_mean = input(
                "Masukkan deret bilangan (*pisahkan dengan koma) :")
            data = []

            for bilangan in data_mean.split(","):
                data.append(int(bilangan))

            mean = statistics.mean(data)
            print(f"Data = {data}")
            print(f"Mean = {mean}")
        elif mmm == 2:
            data_median = input(
                "Masukkan deret bilangan (*pisahkan dengan koma) :")
            data = []

            for bilangan in data_median.split(","):
                data.append(int(bilangan))

            median = statistics.median(data)
            print(f"Data = {data}")
            print(f"Median = {median}")
        elif mmm == 3:
            data_modus = input(
                "Masukkan deret bilangan (*pisahkan dengan koma) :")
            data = []

            for bilangan in data_modus.split(","):
                data.append(int(bilangan))

            modus = statistics.mode(data)
            print(f"Data = {data}")
            print(f"Modus = {modus}")
        else:
            print("Data tidak valid")

    elif jenis_matematika == 5:
        print(30*"=")
        print("Mencari Volume Balok")
        p = float(input("Masukkan nilai panjang :"))
        l = float(input("Masukkan nilai lebar :"))
        t = float(input("Masukkan nilai tinggi :"))
        volume = p * l * t
        print("Volume balok adalah :", volume)

    else:
        print("Mohon maaf jenis matematika yang anda pilih untuk saat ini belum tersedia.")


elif jenis_kalkulator == 2:
    print("1. Kecepatan")
    print("2. Waktu tempuh")
    print("3. Massa jenis")
    print("4. Tegangan listrik")
    print("5. BMI (Body Mass Index)")
    jenis_fisika = int(input("Pilih salah satu jenis fisika [1/2/3/4/5] :"))
    if jenis_fisika == 1:
        print(30*"=")
        print("Menghitung Kecepatan")
        s = float(input("Masukkan nilai jarak (km) :"))
        t = float(input("Masukkan nilai waktu tempuh (jam) :"))
        v = s / t
        print("Kecepatan benda tersebut adalah", v, "km/jam")
    elif jenis_fisika == 2:
        print(30*"=")
        print("Menghitung Waktu Tempuh")
        s = float(input("Masukkan nilai jarak (km) :"))
        v = float(input("Masukkan nilai kecepatan (km/jam) :"))
        t = s / v
        print("Waktu tempuh benda tersebut adalah", t, "jam")
    elif jenis_fisika == 3:
        print(30*"=")
        print("Menghitung Massa Jenis")
        m = float(input("Masukkan nilai massa (kg) :"))
        v = float(input("Masukkan nilai volume (m^3) :"))
        rho = m / v
        print("Massa jenis benda tersebut adalah", rho, "kg/m^3")
    elif jenis_fisika == 4:
        print(30*"=")
        print("Menghitung Tegangan Listrik")
        i = float(input("Masukkan nilai kuat arus (ampere) :"))
        r = float(input("Masukkan nilai hambatan (ohm) :"))
        v = i * r
        print("Tegangan listrik benda tersebut adalah", v, "volt")
    elif jenis_fisika == 5:
        print(30*"=")
        print("Menghitung BMI")
        tb = float(input("Masukkan tinggi badan (m) :"))
        bb = float(input("Masukkan berat badan (kg) :"))
        bmi = bb / (tb * tb)
        print("Nilai BMI anda adalah %2f" % bmi)
        print(30*"=")
        print("Di bawah 18,5 = Berat badan kurang")
        print("18,5 – 22,9 = Berat badan normal")
        print("23 – 29,9 = Berat badan berlebih (kecenderungan obesitas)")
        print("30 ke atas = obesitas")

    else:
        print("Mohon maaf jenis fisika yang anda pilih untuk saat ini belum tersedia.")

elif jenis_kalkulator == 3:
    print("Nama Program : Kalkulator")
    print("Versi : 1.0.0")
    print("Dibuat pada : 30 Des 2021")
    print("Dibuat Oleh : Hikmalul A'la Syahrizaldy")
    print("Asal :Cibenon, Kec. Sidareja, Kab. Cilacap")
    print("Study : Universitas Amikom Purwokerton - Teknologi Informasi \n\r")
    print("Apabila anda menemukan bug atau saran update")
    print("Hubungi nomor :083851117419 atau ig = @hikmal_a.s")
    print(" "*10, "Terima Kasih...>_<")


else:
    print("-> Mohon maaf jenis kalkulator yang anda pilih untuk saat ini belum tersedia. <- \n\r")
    print("Mungkin anda bisa mensupport pengembang agar segera melakukan update.")
    print("Apabila anda menemukan bug atau saran update")
    print("Hubungi nomor :083851117419 atau ig = @hikmal_a.s")
    print(">"*10, "Terima Kasih", "<"*10)
