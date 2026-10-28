from pathlib import Path

from src.proses import status_lulus


def tampilkan_laporan(data_nilai, hasil):
    laporan = []

    laporan.append("LAPORAN REKAP DAN ANALISIS NILAI MATEMATIKA")
    laporan.append("=" * 50)
    laporan.append("")

    laporan.append("Daftar Nilai Siswa:")
    laporan.append("-" * 50)

    for data in data_nilai:
        status = status_lulus(data["nilai"])

        laporan.append(
            f"{data['id']} | {data['nama']} | "
            f"{data['nilai']:.2f} | {status}"
        )

    laporan.append("")
    laporan.append("Ringkasan Nilai:")
    laporan.append("-" * 50)
    laporan.append(f"Jumlah siswa       : {hasil['jumlah_siswa']}")
    laporan.append(f"Rata-rata nilai    : {hasil['rata_rata']:.2f}")
    laporan.append(f"Nilai tertinggi    : {hasil['nilai_tertinggi']:.2f}")
    laporan.append(f"Nilai terendah     : {hasil['nilai_terendah']:.2f}")
    laporan.append(f"Jumlah siswa lulus : {hasil['jumlah_lulus']}")
    laporan.append(
        f"Jumlah tidak lulus : {hasil['jumlah_tidak_lulus']}"
    )

    return "\n".join(laporan)


def simpan_laporan(laporan, lokasi_file):
    lokasi_file = Path(lokasi_file)

    lokasi_file.parent.mkdir(parents=True, exist_ok=True)

    with open(lokasi_file, "w", encoding="utf-8") as file:
        file.write(laporan)