# Untuk mengembalikan banyak nilai
# return x, n menggunakan tanda koma
# dan hasil returnnya bertipe tuple


def min_max(values: list) -> tuple:
    """ini adalah sebuah fungsi untuk mencari
    nilai terkecil dan terbesar dari sebuah list.
    """
    min = values[0]
    max = values[-1]
    return min, max


values = [0, 1, 2, 3, 4, 5]
mm = min_max(values=values)  # Bisa menggunakan tanda sama dengan
print(type(mm))
print(mm)


a = min_max()
