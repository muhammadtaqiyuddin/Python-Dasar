# data yang dimasukkan pasti string
data = input("Masukkan data: ")
print("data = ", data,",type = ",type(data))

#jika kita ingin mengambil int, maka

angka = int (input("masukkan angka: "))
angka = float (input("masukkan angka: "))

print("data = ", angka,",type = ",type(angka))

#bagaimana dengan boolean

biner = bool(int(input("masukkan nilai boolean: ")))
print("data = ", biner,",type = ",type(biner))