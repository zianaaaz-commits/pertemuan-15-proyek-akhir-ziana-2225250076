BATAS_LULUS = 60
NILAI_MINIMUM = 0
NILAI_MAKSIMUM = 100


def validasi_data(data_nilai):
    data_valid = []
    daftar_error = []

    for data in data_nilai:
        nilai = data["nilai"]

        if NILAI_MINIMUM <= nilai <= NILAI_MAKSIMUM:
            data_valid.append(data)
        else:
            daftar_error.append(
                f"Nilai {data['nama']} harus berada pada rentang 0–100."
            )

    return data_valid, daftar_error


def status_lulus(nilai):
    if nilai >= BATAS_LULUS:
        return "Lulus"

    return "Tidak Lulus"


def ringkasan(data_nilai):
    if not data_nilai:
        return {
            "jumlah_siswa": 0,
            "rata_rata": 0,
            "nilai_tertinggi": 0,
            "nilai_terendah": 0,
            "jumlah_lulus": 0,
            "jumlah_tidak_lulus": 0
        }

    daftar_nilai = [data["nilai"] for data in data_nilai]

    jumlah_lulus = sum(
        1 for nilai in daftar_nilai
        if status_lulus(nilai) == "Lulus"
    )

    jumlah_tidak_lulus = len(daftar_nilai) - jumlah_lulus

    return {
        "jumlah_siswa": len(data_nilai),
        "rata_rata": sum(daftar_nilai) / len(daftar_nilai),
        "nilai_tertinggi": max(daftar_nilai),
        "nilai_terendah": min(daftar_nilai),
        "jumlah_lulus": jumlah_lulus,
        "jumlah_tidak_lulus": jumlah_tidak_lulus
    }