# fungsi menggunakan *args
# def ngeprint(*vars):
#     print(type(vars))
#     print(vars)


# ngeprint(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

# Fungsi menggunakan **kwagrs
# def mytest(**kwargs):
#     print(type(kwargs))
#     print(kwargs)


# mytest(nama="Hani", umur=40, dewasa=True)


def test(*args, **kwargs):
    x = args[0]
    y = args[1]

    tipe = kwargs.get("tipe")
    if tipe == None:
        raise ValueError("Harap masukkan paramater tipe.")
    if tipe == "tambah":
        return x + y
    if tipe == "kurang":
        return x - y


hasil = test(10, 5)
print(hasil)
