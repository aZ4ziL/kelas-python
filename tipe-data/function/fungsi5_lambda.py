"""
Lambda expression di Python adalah sebuah ekspresi untuk membuat fungsi.

Lambda sendiri berasal dari teori kalkulus, yakni Lambda Calculus 
yang dikenalkan oleh Alonzo Church di tahun 1930.

Berkat lambda, kita bisa membuat fungsi tanpa nama atau dikenal juga dengan anonymous function.
"""

# contoh fungsi biasa
def square_sum(x, y):
    return x**2 + y**2


# Jika menggunakan lambda tidak menggunakan def dan return
terserah = lambda x, y: x**2 + y**2
print(terserah(10, 10))
