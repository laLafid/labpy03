saldo = 1000000
while True:
    print(f"Saldo Anda : {saldo} \n1. Tarik Tunai\n2. Keluar")
    pilihan = input("Masukan Pilihan : ").lower()
    if pilihan in ['1', 'tarik tunai', 'tarik']:
        while True:
            nominal = int(input("Masukan Nominal : "))
            if nominal > saldo:
                print("Saldo Anda Tidak Cukup")
            else:
                saldo = saldo - nominal
                print(f"Saldo Anda Sekarang : {saldo}")
                break
    elif pilihan in ['2', 'keluar']:
        print("Terima Kasih")
        break
    else:
        print("Pilihan Tidak Tersedia")