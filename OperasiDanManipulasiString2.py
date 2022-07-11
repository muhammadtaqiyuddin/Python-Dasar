# operator dalam bentuk method

## merubah case dari string

# merubah semua ke upper case

salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# mengubah semua ke lower case
alay = "aKu KeCe AbieZzzZ"
print("normal = " + alay)
alay = alay.lower()
print("Lower = " + alay)

## pengecekan dengan isX method
# contoh pengecekan lower case
salam = "sist"
apakah_lower = salam.islower() # hasilnya bool
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper() # hasilnya bool
print(salam + " is upper = " + str(apakah_upper))

# isalpha() <-- untuk mengecek semuanya huruf
# isalnum() <-- huruf dan angka 
# isdecimal() <-- angka saja
# isspace() <-- spasi,tab,newline \n
# istitle() <-- semua kata dimulai dengan huruf besar

judul = "It Is Okay No To Be Orkay"
cek_judul = judul.istitle() # hasil bool
print(judul + "is title = " + str(cek_judul))

## ngecek komponen startswith() endswi() <-- keren
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start = " + str(cek_start))

cek_end = "Sangjangnim Oppak".endswith("Oppak")
print("end = " + str(cek_end))

## penggabungan komponen join() split()
pisah = ['aku', 'sayang','kamu']
gabung = ','.join(pisah)
print(pisah)
print(gabung)

gabung = ' '.join(pisah)
print(gabung)

gabung = "akuehemsayangehemkamu"
print(gabung.split('ehem'))

# alokasi karakter rjust(), ljust(). center()
print(5*"=" + " data " + "="*5)
kanan = "kanan".rjust(10)
print("'" + kanan + "'")

kiri = "kiri".ljust(10)
print("'" + kiri + "'")

tengah = "tengah".center(10,"-")
print("'" + tengah + "'")

# kebalikannnya -> strip()
tengah = tengah.strip("-") # menghilangkan tanda - 
print("'"+tengah+"'")
