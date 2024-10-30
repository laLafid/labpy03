def hitung_keuntungan(modal_awal):

  persentase_keuntungan = [0, 0, 0.01, 0.01, 0.05, 0.05, 0.05, -0.02]

  total_keuntungan = 0

  for i, persentase in enumerate(persentase_keuntungan, start=1):
    keuntungan_bulan_ini = modal_awal * persentase
    total_keuntungan += keuntungan_bulan_ini
    modal_awal += keuntungan_bulan_ini
    print(f"Keuntungan bulan ke-{i} adalah: {keuntungan_bulan_ini:.2f}")

  return total_keuntungan

modal_awal = 100000000

total_keuntungan = hitung_keuntungan(modal_awal)
print("Total keuntungan selama 8 bulan adalah:", total_keuntungan)
