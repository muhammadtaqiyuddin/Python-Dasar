# 1. menyambung string (concatenate)
nama_pertama = "Muhammad"
nama_tengah = "Taqi"
nama_akhir = "Yuddin"

nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_akhir
print(nama_lengkap)

# 2. Menghitung panjang dari string
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " = " + str(panjang) )

# 3. operator untuk string

#mengecek apakah ada komponen char atau string di string

d = "Taqi"
status = d in nama_lengkap
print( d + " ada di " + nama_lengkap + " = " + str(status))


D = "Taqi"
status = D in nama_lengkap
print( D + " ada di " + nama_lengkap + " = " + str(status))

d = "Taqi"
status = d not in nama_lengkap
print( d + " tidak  ada di " + nama_lengkap + " = " + str(status))

# mengulang string
print("WK"*10)
print(100*"WK")

# indexing
print("index ke-0: " + nama_lengkap[0])
print("index ke-1: " + nama_lengkap[1])
print("index ke-7: " + nama_lengkap[7])
print("index ke-(-1): " + nama_lengkap[-1])
print("index ke-(-2 ): " + nama_lengkap[-2])
print("index ke-[0:3]:" + nama_lengkap[0:4])
print("index ke-[0:2:4:8:10]:" + nama_lengkap[0:10:2])

# item paling kecil
print("paling kecil : " + min(nama_lengkap))

# item paling Besar
print("paling Besar : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))

data = 117
print("Char untuk ASCII 117 adalah " + chr(data))

# 4. operator dalam bentuk method
data = "mukhsin aryadul jinan"
jumlah = data.count("i")
print("jumlah i pada " + data + " = " + str(jumlah
))