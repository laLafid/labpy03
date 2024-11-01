import random

while True:
    print("Masukan jumlah")
    try:
        jumlah = int(input('Jumlah data : '))
        if jumlah > 0:
            break
        else:
            print("Masukan nilai lebih besar dari 0! silahkan coba lagi")
    except ValueError:
        print("!Masukan angka! silahkan coba lagi")
        
for data in range(jumlah):
    a = random.uniform(0, 0.5)
    print(f"Data ke {data+1} => {a}")