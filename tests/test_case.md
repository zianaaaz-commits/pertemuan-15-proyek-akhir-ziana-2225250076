# Test Case

| Kode | Skenario Pengujian | Hasil yang Diharapkan | Status |
|---|---|---|---|
| TC01 | Memasukkan data nilai yang valid | Data berhasil dibaca dan diproses | PASS |
| TC02 | Memasukkan nilai 0 | Nilai diterima sebagai nilai minimum | PASS |
| TC03 | Memasukkan nilai 100 | Nilai diterima sebagai nilai maksimum | PASS |
| TC04 | Memasukkan nilai di bawah 0 | Data ditolak karena nilai di luar rentang | PASS |
| TC05 | Memasukkan nilai di atas 100 | Data ditolak karena nilai di luar rentang | PASS |
| TC06 | Memasukkan data nilai berupa huruf | Data ditolak karena nilai harus berupa angka | PASS |
| TC07 | Menggunakan file data kosong | Program menampilkan pesan tidak ada data nilai yang valid | PASS |
| TC08 | Menggunakan file data yang tidak ditemukan | Program menampilkan pesan file tidak ditemukan | PASS |