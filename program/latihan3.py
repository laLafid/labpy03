saldo = 1000000
while True:
    print(f"Saldo Anda : {saldo} \n1. Tarik Tunai\n2. Keluar")
    pilihan = int(input("Masukan Pilihan : "))
    if pilihan == 1:
        nominal = int(input("Masukan Nominal : "))
        if nominal > saldo:
            print("Saldo Anda Tidak Cukup")
        else:
            saldo = saldo - nominal
            print(f"Saldo Anda Sekarang : {saldo}")
    elif pilihan == 2:
        print("Terima Kasih")
        break
    else:
        print("Pilihan Tidak Tersedia")