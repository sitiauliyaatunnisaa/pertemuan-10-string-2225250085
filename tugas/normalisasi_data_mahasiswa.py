
# Input: Nama lengkap dan kode kelas dari pengguna.
# Proses: Menormalisasi nama, membuat inisial, dan merapikan kode kelas.
# Output: Nama bersih, kode kelas, jumlah kata, dan inisial.

def normalisasi_nama(nama):
    """Membersihkan spasi dan mengubah nama menjadi title case."""
    return " ".join(nama.strip().split()).title()


def buat_inisial(nama):
    """Membuat inisial dari huruf pertama setiap kata."""
    kata = normalisasi_nama(nama).split()
    return "".join(k[0] for k in kata)


def normalisasi_kode(kode):
    """Mengubah kode kelas menjadi huruf besar dengan tanda hubung."""
    kata = kode.strip().upper().split()
    return "-".join(kata)


# Menerima input pengguna
nama = input("Nama: ")
kode = input("Kode kelas: ")

# Mengolah data
nama_bersih = normalisasi_nama(nama)
kode_bersih = normalisasi_kode(kode)
jumlah_kata = len(nama_bersih.split())
inisial = buat_inisial(nama)

# Menampilkan hasil
print(f"Nama bersih : {nama_bersih}")
print(f"Kode kelas  : {kode_bersih}")
print(f"Jumlah kata : {jumlah_kata}")
print(f"Inisial     : {inisial}")
