"""
Inner function, juga dikenal sebagai fungsi bersarang , adalah fungsi yang Anda 
tetapkan di dalam fungsi lain. Di Python, fungsi semacam ini memiliki akses langsung 
ke variabel dan nama yang ditentukan dalam fungsi terlampir. 
Fungsi bagian dalam memiliki banyak kegunaan, terutama sebagai pabrik penutup
dan fungsi dekorator.
"""


# def outer_func(who):
#     def inner_func():
#         print(f"Hello, {who}")

#     inner_func()


# outer_func("World")


def factorial(number):
    if not isinstance(number, int):
        raise TypeError("Sorry, 'number' must be an integer.")
    if number < 0:
        raise ValueError("Sorry, 'number' must be zero or positive.")

    def inner_factorial(number):
        if number <= 1:
            return 1
        return number * inner_factorial(number - 1)

    return inner_factorial(number)


print(factorial(5))
