
# Input: Kalimat dan kata yang akan dicari.
# Proses: Mengubah teks menjadi huruf kecil, lalu mencari kata.
# Output: Status keberadaan, jumlah kemunculan, dan posisi pertama.

teks = "Python untuk data. Python untuk pendidikan."
teks = teks.lower()
kata = "python"

print(kata in teks)
print(teks.count(kata))
print(teks.find(kata))
