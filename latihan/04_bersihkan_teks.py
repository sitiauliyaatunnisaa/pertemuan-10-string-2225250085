
# Input: Kalimat dengan spasi berlebih.
# Proses: Menghapus spasi tepi dan merapikan spasi antarkata.
# Output: Kalimat dengan kapitalisasi awal.

teks = " belajar    python  untuk           pendidikan       "
teks = teks.strip()

while "  " in teks:
    teks = teks.replace("  ", " ")

print(teks.capitalize())
