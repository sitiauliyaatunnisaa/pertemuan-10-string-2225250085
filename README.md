# Pertemuan 10 - String dan Pengolahan Teks

**Nama:** Siti Auliyaatunnisaa  
**NIM:** 2225250085  
**Kelas:** 3A

## Tujuan

Mempelajari penggunaan string Python untuk mengakses karakter, mengambil sebagian teks, mengubah kapitalisasi, membersihkan spasi, memisahkan dan menggabungkan kata, serta melakukan pencarian teks. Materi ini juga diterapkan untuk menormalisasi data nama mahasiswa dan kode kelas.

## Struktur Program

Folder `latihan/` berisi enam program latihan, yaitu dasar string, indeks dan slicing, method string, pembersihan teks, split dan join, serta pencarian kata.

Folder `tugas/` berisi program `normalisasi_data_mahasiswa.py` untuk membersihkan nama mahasiswa, menormalisasi kode kelas, menghitung jumlah kata, dan membentuk inisial menggunakan fungsi Python.

## Algoritma Tugas 4

1. Menerima input nama mahasiswa dan kode kelas.
2. Membersihkan nama menggunakan `strip()`, `split()`, dan `title()`.
3. Membuat inisial dari huruf pertama setiap kata.
4. Mengubah kode kelas menjadi huruf besar dan menggabungkan kata dengan tanda hubung.
5. Menghitung jumlah kata pada nama yang sudah dibersihkan.
6. Menampilkan nama bersih, kode kelas, jumlah kata, dan inisial.

## Cara Menjalankan

Jalankan setiap latihan dari terminal VS Code pada folder utama proyek.

```bash
python latihan/01_dasar_string.py
python latihan/02_indeks_slicing.py
python latihan/03_method_string.py
python latihan/04_bersihkan_teks.py
python latihan/05_split_join.py
python latihan/06_pencarian_kata.py
```

Untuk menjalankan Tugas 4:

```bash
python tugas/normalisasi_data_mahasiswa.py
```

Jika perintah `python` tidak tersedia, gunakan `python3`.

## Test Case

Pengujian Tugas 4 menggunakan empat data nama dan kode kelas dengan format berbeda.

| No. | Input nama | Input kode | Hasil yang diharapkan |
|---|---|---|---|
| 1 | aan hendrayana | pmat a 2026 | Aan Hendrayana, PMAT-A-2026, 2 kata, AH |
| 2 | fATHIYYAH mUTHMAINNAH | kelas b | Fathiyyah Muthmainnah, KELAS-B, 2 kata, FM |
| 3 | BUDI | pmtk 01 | Budi, PMTK-01, 1 kata, B |
| 4 | siti nur aisyah | kelas c | Siti Nur Aisyah, KELAS-C, 3 kata, SNA |

Hasil aktual dan status pengujian diisi setelah setiap test case dijalankan di VS Code.

## Refleksi

Melalui latihan ini, saya memahami bahwa string merupakan urutan karakter yang dapat diakses menggunakan indeks dan slicing. Method seperti `strip()`, `title()`, dan `upper()` membantu menyeragamkan teks. Saya juga memahami bahwa `split()` dapat memecah teks menjadi list kata, sedangkan `join()` menggabungkan kata menggunakan pemisah tertentu.

Penggunaan fungsi membuat proses normalisasi dapat digunakan kembali sehingga kode lebih terstruktur dan mudah dipelihara.

## Sumber dan Bantuan

Materi utama: Bahan Ajar Algoritma dan Pemrograman, Pertemuan 10 - String dan Pengolahan Teks dalam Python.

Bantuan AI digunakan untuk membantu penyusunan dan penjelasan kode serta dokumentasi. Seluruh program dan hasil pengujian perlu diperiksa kembali oleh mahasiswa.