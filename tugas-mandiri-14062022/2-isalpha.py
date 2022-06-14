inp = input("Inputan: ")
angka = 0
kata = 0

for x in inp:
    if x.isdigit():
        angka += 1
    if x.isalpha():
        kata += 1

print("Kata: ", kata)
print("Angka: ", angka)