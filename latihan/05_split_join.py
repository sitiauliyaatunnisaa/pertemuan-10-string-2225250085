
# Input: Kalimat yang terdiri dari beberapa kata.
# Proses: Memecah kalimat menjadi list kata dan menggabungkannya dengan tanda hubung.
# Output: List kata dan kalimat dengan pemisah tanda hubung.

kalimat = "data teks perlu dibersihkan"
kata = kalimat.split()

print(kata)
print("-".join(kata))
