import matplotlib.pyplot as plt
import numpy as np
from datetime import date

class Siswa:
    def __init__(self):
        self.__nama__ = "nama"
        self.__npm__ = "npm"
        self.__kelas__ = "kelas"
        self.__tinggi__ = 160
        self.__berat__ = 50
        self.__tanggal_lahir__ = date(2000, 12, 31)

    def set_nama(self, nama):
        self.__nama__ = nama

    def set_npm(self, npm):
        self.__npm__ = npm

    def set_kelas(self, kelas):
        self.__kelas__ = kelas

    def set_tinggi(self, tinggi):
        self.__tinggi__ = int(tinggi)

    def set_berat(self, berat):
        self.__berat__ = int(berat)

    def set_tanggal_lahir(self, tanggal):
        _tanggal_ = tanggal.split("/")
        self.__tanggal_lahir__ = date(int(_tanggal_[2]), int(_tanggal_[0]), int(_tanggal_[1]))

    def get_nama(self):
        return self.__nama__

    def get_npm(self):
        return self.__npm__

    def get_kelas(self):
        return self.__kelas__

    def get_tinggi(self):
        return self.__tinggi__

    def get_berat(self):
        return self.__berat__

    def get_tanggal_lahir(self):
        return self.__tanggal_lahir__

list_siswa = []

with open('data.csv', 'r') as input_data:
    next(input_data)
    for line in input_data:
        kolom = line.split(",")
        siswa = Siswa()
        siswa.set_npm(kolom[2])
        siswa.set_nama(kolom[3])
        siswa.set_kelas(kolom[4])
        siswa.set_tanggal_lahir(kolom[5])
        siswa.set_tinggi(kolom[6])
        siswa.set_berat(kolom[7])
        list_siswa.append(siswa)

with open('OUTPUT.TXT', 'w') as f:
    for siswa in list_siswa:
        npm = siswa.get_npm()
        nama = siswa.get_nama()
        kelas = siswa.get_kelas()
        line_data = [npm, "\t", nama, "\t", kelas, "\n"]
        f.writelines(line_data)

count_20 = 0
for siswa in list_siswa:
    tanggal_acuan = date(2024, 3, 15)
    tanggal_lahir = siswa.get_tanggal_lahir()
    usia = tanggal_acuan.year - tanggal_lahir.year
    if usia >= 20:
        count_20 += 1

print("Jumlah siswa yang sudah berusia 20 tahun pada tahun 2024:", count_20)
