laba = [0, 0, 0.01, 0.01, 0.05, 0.05, 0.05, -0.02]
saldo = 100_000_000
total = 0

for bulan, laba_bulan in enumerate(laba, start=1):
    laba_bulan = saldo * laba_bulan
    total += laba_bulan
    print(f"Keuntungan bulan ke {bulan} adalah: {laba_bulan}")

print(f"total laba {total}")
print(f"total saldo menjadi {total + saldo}")