"""
Parameter adalah suatu variabel yang berfungsi untuk menampung 
nilai yang akan dikirimkan ke dalam fungsi. 
Dengan adanya parameter, sebuah fungsi dapat bersift dinamis.
"""


# def tambah(x, y):
#     hasil = x + y
#     print(hasil)


# tambah(1, 2)
# tambah(2, 3)
# tambah(3, 4)
# tambah(4, 5)


print()


# def luas_segitiga(alas: int, tinggi: int) -> float:
#     luas = (alas * tinggi) / 2
#     return luas


# a = luas_segitiga(5, 10)
# b = luas_segitiga(5, 20)
# print(a)
# print(b)
# print(luas_segitiga(10, 10))


# Fungsi default value
def bio(nama, umur, jk="Laki-laki", warna="Merah"):
    print(nama, umur, jk)


# bio("Susi", 18)

bio(umur=18, nama="Juni", jk="Perempuan")
