import random

while True:
    print("Masukan jumlah")
    try:
        jumlah = int(input('Jumlah data : '))
        if jumlah > 0:
            break
        else:
            print("masukan nilai lebih dari 0, silahkan coba lagi")
    except ValueError:
        print("tidak bisa memilih itu, silahkan coba lagi")

for i in range(jumlah):
    a = random.uniform(0, 0.5)
    print(f'Data ke {i+1} => {a}')