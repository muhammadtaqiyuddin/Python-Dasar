from re import L


print('===== LATIHAN STRING 1 =====')

name = 'John Doe' 
message = "John Doe belajar bahasa pyhtone di Belajarpython"
print ("name[0]: ",name[0])
print ("message[1:4]: ",message[1:4])

print('===== LATIHAN STRING 2 =====')
message = 'Hello World'
print ("Update String :- ", message[:6] + 'Python')

print('===== LATIHAN LIST 1 =====')
list1 = ['fisika','kimia',1993,2017]
list2 = [1,2,3,4,5,6,7]
print ("list1[0]: ",list1[0])

print('===== LATIHAN LIST 2 =====')
list = ['fisika','kimia',1993,2017]
print("Nilai ada pada index 2 : ",list[2])
list[2] = 2001
print("Nilai baru ada pada index 2 : ",list[2])

print('===== LATIHAN LIST 3 =====')
list = ['fisika','kimia',1993,2017]
print (list)
del list[2]
print ("Setelah dihapus nilai pada index 2 : ",list)