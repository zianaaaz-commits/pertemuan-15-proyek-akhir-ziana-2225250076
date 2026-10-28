from pathlib import Path


def baca_data_nilai(lokasi_file):
    data_nilai = []
    daftar_error = []

    lokasi_file = Path(lokasi_file)

    if not lokasi_file.exists():
        return [], [f"File tidak ditemukan: {lokasi_file}"]

    with open(lokasi_file, "r", encoding="utf-8") as file:
        for nomor_baris, baris in enumerate(file, start=1):
            baris = baris.strip()

            if not baris:
                continue

            bagian = baris.split(",")

            if len(bagian) != 3:
                daftar_error.append(
                    f"Baris {nomor_baris}: format data tidak sesuai."
                )
                continue

            id_siswa, nama, nilai = bagian

            try:
                nilai = float(nilai)
            except ValueError:
                daftar_error.append(
                    f"Baris {nomor_baris}: nilai harus berupa angka."
                )
                continue

            data_nilai.append({
                "id": id_siswa.strip(),
                "nama": nama.strip(),
                "nilai": nilai
            })

    return data_nilai, daftar_error