from pathlib import Path

from src.input_data import baca_data_nilai
from src.proses import validasi_data, ringkasan
from src.output import tampilkan_laporan, simpan_laporan


def main():
    folder_proyek = Path(__file__).parent

    file_data = folder_proyek / "data" / "contoh_data.txt"
    file_output = folder_proyek / "output" / "laporan_nilai.txt"

    data_nilai, error_input = baca_data_nilai(file_data)

    data_valid, error_validasi = validasi_data(data_nilai)

    daftar_error = error_input + error_validasi

    if daftar_error:
        print("Data yang tidak dapat diproses:")

        for error in daftar_error:
            print(f"- {error}")

    if not data_valid:
        print("\nTidak ada data nilai yang valid.")
        return

    hasil = ringkasan(data_valid)

    laporan = tampilkan_laporan(data_valid, hasil)

    print(laporan)

    simpan_laporan(laporan, file_output)

    print(f"\nLaporan berhasil disimpan di: {file_output}")


if __name__ == "__main__":
    main()