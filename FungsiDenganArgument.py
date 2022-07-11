# Template
# def nama_fungsi(argument):
#     Badan fungsi


def hello_world(nama):
    '''fungsi hello world menerima input dengan variable nama'''
    print(f"Selamat datang dunia wahai {nama}")


hello_world("taqi")
hello_world("mukhsin")

# program tambah

def tambah(angka_1,angka_2):
    '''fungsi tambah'''
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")

tambah(1,5)
tambah(100000,1)

def say_hi(list_peserta):
    '''fungsi say hi'''
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"Yang terhormat {peserta}")

anggota_boyband = ["taqi","yuddin","zaky"]

say_hi(anggota_boyband)