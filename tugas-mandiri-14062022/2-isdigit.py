inp = input("Inputan: ")
angka = 0

for x in inp:
    if x.isdigit():
        angka += 1

print("Jumlah Angka: ", angka)