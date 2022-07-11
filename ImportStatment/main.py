# import

# fungsinya adalah untuk mengambil 
# program dari file external .py

# 1. untuk menyambung program dari external
import program_print
import program_mukhsin

# 2. import dengan data
import variable
import taqi

# data ada di namespace variable
print(variable.data)
print(taqi.data)

# 3. import dengan fungsi
import matematika

hasil = matematika.tambah(4,5)
print(hasil)