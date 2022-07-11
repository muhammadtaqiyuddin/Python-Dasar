
data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string
'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."
'''

data = 'menggunakan single quote'
print(data)

data = "menggunakan double quote"
print(data)

print('"Hallo, apa kabar ?"')
print("'Hallo, apa kabar ?'")
print("ini adalah hari jum'at")

# 2. Menggunakan tanda \

# membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day,isn\'t it?')

#backlash
print("C:\\user\\Taqi")

# tab
print("Taqi\tyuddin")

#backspace
print("taqi \byuddin")

#newLine
print("baris pertama.\nbaris kedua.")#LF -> Line Feed ->unix,macos,linux
print("baris pertama.\rbaris kedua.")# CR -> carriage return -> commodore,acorn,lisp
print("baris pertama.\r\nbaris kedua.") # CRLF -> line feed carrriage return -> dipakai oleh windows

# 3. string Literal atau raw 

# hati-hati
print('C:\\new folder') 

# menggunakan raw string
print(r'C:\new folder')

# multiline literal string
print("""
Nama : Muhammad Taqiyuddin
Kelas : IF 07
""")

# multiline literal string dan RAW
print(r"""
Nama : Muhammad Taqiyuddin
Kelas : IF 07
website : www.mtaqiyuddin.com/newID
""")