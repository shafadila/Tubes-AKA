import time
import matplotlib.pyplot as plt
from prettytable import PrettyTable

def penyebaran_dbd_rekursif(kepadatan_penduduk, suhu_rata_rata, kelembapan_udara, dbd_dict, index=0):
    keys = list(dbd_dict.keys())
    if index >= len(keys):
        return "Tidak ditemukan tingkat penyebaran"
    if kepadatan_penduduk <= keys[index][0] and suhu_rata_rata <= keys[index][1] and kelembapan_udara <= keys[index][2]:
        return dbd_dict[keys[index]]
    return penyebaran_dbd_rekursif(kepadatan_penduduk, suhu_rata_rata, kelembapan_udara, dbd_dict, index + 1)

def penyebaran_dbd_iteratif(kepadatan_penduduk, suhu_rata_rata, kelembapan_udara, dbd_dict):
    for (batas_kepadatan, batas_suhu, batas_kelembapan), tingkat in dbd_dict.items():
        if kepadatan_penduduk <= batas_kepadatan and suhu_rata_rata <= batas_suhu and kelembapan_udara <= batas_kelembapan:
            return tingkat
    return "Tidak ditemukan tingkat penyebaran"

dbd_dict = {
    (10000, 30, 70): "Rendah", (15000, 32, 75): "Sedang", (20000, 35, 80): "Tinggi",
    (25000, 37, 85): "Sangat Tinggi", (30000, 40, 90): "Ekstrem"
}

daftar_kota = []
daftar_kepadatan_penduduk = []
daftar_suhu_rata_rata = []
daftar_kelembapan_udara = []
total_waktu_rekursif = []
total_waktu_iteratif = []
daftar_tingkat_rekursif = []
daftar_tingkat_iteratif = []

def print_execution_table():
    table = PrettyTable()
    table.field_names = ["Kota", "Kepadatan Penduduk", "Suhu Rata-rata", "Kelembapan Udara", "Tingkat Penyebaran", "Waktu Rekursif (s)", "Waktu Iteratif (s)"]
    for i in range(len(daftar_kota)):
        table.add_row([daftar_kota[i], daftar_kepadatan_penduduk[i], daftar_suhu_rata_rata[i], daftar_kelembapan_udara[i], daftar_tingkat_rekursif[i], total_waktu_rekursif[i], total_waktu_iteratif[i]])
    print(table)

def update_graph():
    plt.figure(figsize=(8, 6))
    plt.plot(daftar_kota, total_waktu_rekursif, label='Recursive', marker='o', linestyle='-')
    plt.plot(daftar_kota, total_waktu_iteratif, label='Iterative', marker='o', linestyle='-')
    plt.title('Performance Comparison: Recursive vs Iterative')
    plt.xlabel('Input (Kota)')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.show(block=False)
    plt.pause(0.1)

while True:
    try:
        kota = input("Masukkan nama kota (atau ketik 'selesai' untuk keluar): ")
        if kota.lower() == "selesai":
            break
        kepadatan_penduduk = float(input("Masukkan kepadatan penduduk (per km2): "))
        suhu_rata_rata = float(input("Masukkan suhu rata-rata (dalam °C): "))
        kelembapan_udara = float(input("Masukkan kelembapan udara (dalam %): "))


        daftar_kota.append(kota)
        daftar_kepadatan_penduduk.append(kepadatan_penduduk)
        daftar_suhu_rata_rata.append(suhu_rata_rata)
        daftar_kelembapan_udara.append(kelembapan_udara)

start_rekursif = time.time()
        tingkat_rekursif = penyebaran_dbd_rekursif(kepadatan_penduduk, suhu_rata_rata, kelembapan_udara, dbd_dict)
        end_rekursif = time.time()
        waktu_rekursif = end_rekursif - start_rekursif
        total_waktu_rekursif.append(waktu_rekursif)


        start_iteratif = time.time()
        tingkat_iteratif = penyebaran_dbd_iteratif(kepadatan_penduduk, suhu_rata_rata, kelembapan_udara, dbd_dict)
        end_iteratif = time.time()
        waktu_iteratif = end_iteratif - start_iteratif
        total_waktu_iteratif.append(waktu_iteratif)

daftar_tingkat_rekursif.append(tingkat_rekursif)
        daftar_tingkat_iteratif.append(tingkat_iteratif)


        print_execution_table()
        update_graph()

    except ValueError:
        print("Masukkan nilai yang valid!")
