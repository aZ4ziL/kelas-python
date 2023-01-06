from greeting.hello import Hello

h = Hello("Yasir")

print(h.hello())

if Hello.is_adult(22):
    print("Kamu dewasa")
else:
    print("Kamu bocil")
