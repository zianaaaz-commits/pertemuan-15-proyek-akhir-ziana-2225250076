# Program Rekap dan Analisis Nilai Matematika Kelas

## Identitas Proyek

- **Nama:** Ziana Alfia Zahra
- **NIM:** 2225250076
- **Kelas:** 3A
- **Program Studi:** Pendidikan Matematika
- **Mata Kuliah:** Algoritma dan Pemrograman
- **Pertemuan:** 15

## Deskripsi Proyek

Program Rekap dan Analisis Nilai Matematika Kelas merupakan program yang digunakan untuk mengolah data nilai siswa.

Program membaca data siswa dari file, melakukan validasi nilai, menghitung rata-rata, menentukan nilai tertinggi dan terendah, serta menentukan status kelulusan berdasarkan KKM.

Hasil pengolahan data ditampilkan pada terminal dan disimpan dalam file laporan.

## Tujuan

1. Mengimplementasikan rancangan proyek dari Pertemuan 14.
2. Mengolah data nilai siswa menggunakan Python.
3. Menerapkan fungsi dan struktur data.
4. Menerapkan pengolahan file.
5. Melakukan pengujian terhadap program.
6. Mendokumentasikan hasil implementasi proyek.

## Fitur Program

1. Membaca data nilai siswa dari file.
2. Memvalidasi nilai siswa pada rentang 0 sampai 100.
3. Menghitung rata-rata nilai.
4. Menentukan nilai tertinggi dan terendah.
5. Menentukan status kelulusan siswa.
6. Menampilkan hasil analisis nilai.
7. Menyimpan laporan hasil analisis ke file.

## Kebutuhan

- Python 3
- Visual Studio Code

## Struktur Folder

```text
pertemuan-15-proyek-akhir-ziana-2225250076/
├── README.md
├── .gitignore
├── main.py
├── src/
│   ├── __init__.py
│   ├── input_data.py
│   ├── proses.py
│   └── output.py
├── data/
│   └── contoh_data.txt
├── tests/
│   └── test_case.md
├── docs/
│   └── screenshot/
└── output/
```

## Cara Menjalankan

1. Buka folder proyek di Visual Studio Code.
2. Pastikan Python 3 sudah tersedia.
3. Buka terminal pada folder proyek.
4. Jalankan perintah berikut:

   ```bash
   python main.py
   ```

5. Program membaca data dari `data/contoh_data.txt`.
6. Hasil analisis ditampilkan pada terminal.
7. Laporan disimpan pada `output/laporan_nilai.txt`.

## Pengujian

Pengujian dilakukan terhadap beberapa kondisi input, yaitu:

- Input data normal.
- Nilai minimum.
- Nilai maksimum.
- Nilai di luar batas.
- Input bukan angka.
- File tidak ditemukan.
- Data kosong.

Hasil pengujian dicatat pada file `tests/test_case.md`.

## Debugging

Apabila ditemukan kesalahan saat program dijalankan, dilakukan pemeriksaan terhadap kode program dan perbaikan pada bagian yang bermasalah.

Program kemudian dijalankan kembali untuk memastikan perbaikan berjalan sesuai kebutuhan.

## Kontribusi

Proyek ini dikerjakan secara individu oleh Ziana Alfia Zahra.

Seluruh proses perancangan, implementasi, pengujian, debugging, dan dokumentasi dilakukan secara mandiri.

# Referensi

- Bahan Ajar Pertemuan 14: Perancangan Proyek dengan VS Code dan GitHub.
- Bahan Ajar Pertemuan 15: Implementasi, Pengujian, dan Dokumentasi Proyek.