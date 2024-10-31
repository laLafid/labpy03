modal_awal = 100_000_000

def hitung_keuntungan(modal_awal):
  laba = [0, 0, 0.01, 0, 0.05, 0, 0, -0.02]
  total = 0
  for i, persentase in enumerate(laba, start=1):
    keuntungan = modal_awal * persentase
    total += keuntungan
    modal_awal += keuntungan
    print(f"Keuntungan bulan ke-{i} adalah: {modal_awal:.2f}")
  return total

total = hitung_keuntungan(modal_awal)
print(f"Modal awal: {modal_awal:.2f}")
print(f"Total keuntungan selama 8 bulan adalah: {total:.2f}")
print(f"Total saldo setelah 8 bulan adalah: {modal_awal + total:.2f}")