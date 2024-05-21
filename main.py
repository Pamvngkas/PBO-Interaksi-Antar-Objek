class Mahasiswa:
    def __init__(self, nama):
        self.nama = nama
        self.nilai = {}

class Dosen:
    def __init__(self, nama):
        self.nama = nama

    def input_nilai(self, mahasiswa, matkul, nilai):
        mahasiswa.nilai[matkul] = nilai

mahasiswa1 = Mahasiswa("Rakha Ukta Pamungkas")

dosen1 = Dosen("Aryudha Jarang Mandi")

dosen1.input_nilai(mahasiswa1, "PBO", 80)
dosen1.input_nilai(mahasiswa1, "Basis Data", 85)

print("Nilai yang diberikan oleh Dosen " + dosen1.nama + " adalah " + mahasiswa1.nama, mahasiswa1.nilai)