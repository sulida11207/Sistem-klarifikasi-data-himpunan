# Sistem Klasifikasi Data dengan Himpunan (PJBL-2)
### Mata Kuliah: Matematika Diskrit - Universitas Bina Bangsa Getsempena (UBBG)

Repositori ini memuat proyek mini sistem klasifikasi data menggunakan pendekatan **Teori Himpunan Diskrit** berbasis bahasa pemrograman Python. Sistem dirancang untuk menguji validitas **Prinsip Inklusi-Eksklusi (PIE)** serta melakukan pembagian segmentasi wilayah saling lepas secara analitis.

## 🚀 Fitur Utama Sistem
1. **Pemodelan Himpunan otomatis** dari dataset tabular `.csv`.
2. **Operasi Aljabar Teori Himpunan Dasar** (`Union`, `Intersection`, `Difference`, `Complement`).
3. **Analisis Matematis Prinsip Inklusi-Eksklusi (PIE)** 3 Himpunan Variabel secara dinamis.
4. **Visualisasi Infografis Otomatis** berupa Diagram Venn 3 lingkaran dan Diagram Batang Distribusi Wilayah Saling Lepas.
5. **Sistem Pengujian Otomatis** langsung pada 2 Skenario Kasus Uji Kampus.

## 📁 Struktur Berkas Proyek
```text
├── data/
│   ├── dataset1_skill_mahasiswa.csv     # Skenario Kasus Uji 1 (Keahlian IT)
│   └── dataset2_minat_studi.csv         # Skenario Kasus Uji 2 (Minat Konsentrasi)
├── main.py                              # Sumber Kode Utama Program Python
├── README.md                            # Dokumentasi Panduan Repositori
├── output_venn_dataset1.png             # Hasil Visualisasi Skenario Uji 1
└── output_venn_dataset2.png             # Hasil Visualisasi Skenario Uji 2
```

## 📊 Ringkasan Hasil Analisis Validasi Matematika
Program membandingkan perhitungan analitis rumus formal PIE dengan nilai total kardinalitas aktual data biner di lapangan:

* **Skenario Kasus 1 (Keahlian IT Mahasiswa):**
  * Total Semesta $|U|$ = 30 Mahasiswa
  * Hasil Rumus PIE = 27 | Hasil Aktual = 27 -> **Status: VALID (True)**
* **Skenario Kasus 2 (Minat Konsentrasi Studi):**
  * Total Semesta $|U|$ = 25 Mahasiswa
  * Hasil Rumus PIE = 23 | Hasil Aktual = 23 -> **Status: VALID (True)**

## 🛠️ Cara Menjalankan Program
Pastikan pustaka `pandas` dan `matplotlib` sudah terpasang di sistem perangkat Anda sebelum menjalankan:
```bash
pip install pandas matplotlib
python main.py
```