#latihan  (date and time)

import datetime as dt

#mendeteksi hari lahir

print (" silahkan masukkan tanggal,bulan dan tahun lahir anda")
tanggal = int(input("masukkan tanggal kelahiran anda   :"))
bulan = int(input("masukkan bulan  kelahiran anda    :"))
tahun = int(input ("masukkan tahun kelahiran andan   :"))

tanggal_lahir = dt.date(tahun,bulan,tanggal)

print( "tanggal lahir anda adalah :",tanggal_lahir )
print ( f"harinya adalah : {tanggal_lahir:%A}")

# menghitung Umur
hari_ini = dt.date.today()
print("hari ini tanggal :", hari_ini)
umur_hari= hari_ini - tanggal_lahir
umur_tahun= umur_hari.days // 360

print (f"umur anda adalah : {umur_tahun} tahun")


       
