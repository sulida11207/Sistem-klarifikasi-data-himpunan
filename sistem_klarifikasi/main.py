import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class SistemKlasifikasiHimpunan:
    def __init__(self, nama_sistem="Sistem Klasifikasi Data"):
        self.nama_sistem = nama_sistem
        self.df = None
        self.himpunan = {}
        self.semesta = set()

    def muat_dataset(self, file_path, id_col="id_mahasiswa", name_col="nama", kolom_kategori=None):
        """Fitur 1: Menerima dataset tabular dan memodelkan kolom menjadi himpunan elemen unik."""
        self.df = pd.read_csv(file_path)
        self.semesta = set(self.df[id_col].astype(str))
        self.himpunan = {}

        if kolom_kategori is None:
            kolom_kategori = [c for c in self.df.columns if c not in [id_col, name_col]]

        for col in kolom_kategori:
            # Memfilter ID entitas yang bernilai 1 (memiliki atribut kategori)
            self.himpunan[col] = set(self.df[self.df[col] == 1][id_col].astype(str))

        print(f"\n[INFO] Dataset '{os.path.basename(file_path)}' berhasil dimuat.")
        print(f"       Total Semesta |U|: {len(self.semesta)} entitas.")
        for k, v in self.himpunan.items():
            print(f"       - Kategori '{k}': {len(v)} anggota.")

    # Fitur 2: Operasi Teori Himpunan Dasar
    def operasi_union(self, A, B): return A | B
    def operasi_intersection(self, A, B): return A & B
    def operasi_difference(self, A, B): return A - B
    def operasi_complement(self, A): return self.semesta - A

    def hitung_inklusi_eksklusi(self, kat_a, kat_b, kat_c):
        """Fitur 4: Perhitungan analitis Prinsip Inklusi-Eksklusi (PIE) & 8 Partisi Disjoin."""
        A, B, C = self.himpunan[kat_a], self.himpunan[kat_b], self.himpunan[kat_c]
        nA, nB, nC = len(A), len(B), len(C)
        nAB, nAC, nBC = len(A & B), len(A & C), len(B & C)
        nABC = len(A & B & C)

        # Rumus PIE 3 Himpunan
        total_pie = nA + nB + nC - (nAB + nAC + nBC) + nABC
        total_aktual = len(A | B | C)

        # 8 Daerah Saling Lepas (Disjoint Regions)
        hanya_ABC = nABC
        hanya_AB = len((A & B) - C)
        hanya_AC = len((A & C) - B)
        hanya_BC = len((B & C) - A)
        hanya_A = len(A - (B | C))
        hanya_B = len(B - (A | C))
        hanya_C = len(C - (A | B))
        di_luar = len(self.semesta - (A | B | C))

        return {
            "kat_a": kat_a, "kat_b": kat_b, "kat_c": kat_c,
            "nA": nA, "nB": nB, "nC": nC,
            "nAB": nAB, "nAC": nAC, "nBC": nBC, "nABC": nABC,
            "total_pie": total_pie, "total_aktual": total_aktual,
            "valid": total_pie == total_aktual, "di_luar": di_luar,
            "hanya_A": hanya_A, "hanya_B": hanya_B, "hanya_C": hanya_C,
            "hanya_AB": hanya_AB, "hanya_AC": hanya_AC, "hanya_BC": hanya_BC,
            "hanya_ABC": hanya_ABC, "total_semesta": len(self.semesta)
        }

    def visualisasi_diagram_venn(self, res, output_path="diagram_venn.png"):
        """Fitur 3: Visualisasi Diagram Venn Otomatis dengan Matplotlib."""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6), gridspec_kw={'width_ratios': [1.2, 1]})

        # Diagram Lingkaran
        ax1.set_xlim(-2.5, 2.5); ax1.set_ylim(-2.5, 2.5); ax1.axis('off')
        box = patches.FancyBboxPatch((-2.3, -2.3), 4.6, 4.6, boxstyle="round,pad=0.1", fc='#F8F9FA', ec='#333', lw=1.5)
        ax1.add_patch(box)
        ax1.text(-2.1, 2.0, f"Semesta U (|U| = {res['total_semesta']})", fontsize=11, weight='bold')

        r = 1.35
        ax1.add_patch(patches.Circle((-0.6, 0.5), r, alpha=0.35, color='#1E88E5', ec='#1565C0', lw=2))
        ax1.add_patch(patches.Circle((0.6, 0.5), r, alpha=0.35, color='#43A047', ec='#2E7D32', lw=2))
        ax1.add_patch(patches.Circle((0.0, -0.6), r, alpha=0.35, color='#FB8C00', ec='#EF6C00', lw=2))

        # Label Wilayah
        ax1.text(-1.4, 1.8, f"Himpunan A\n{res['kat_a']}\n({res['nA']})", ha='center', weight='bold', color='#0D47A1')
        ax1.text(1.4, 1.8, f"Himpunan B\n{res['kat_b']}\n({res['nB']})", ha='center', weight='bold', color='#1B5E20')
        ax1.text(0.0, -2.1, f"Himpunan C: {res['kat_c']} ({res['nC']})", ha='center', weight='bold', color='#E65100')

        # Angka di setiap partisi
        ax1.text(-1.1, 0.6, str(res['hanya_A']), fontsize=13, weight='bold', color='#0D47A1')
        ax1.text(1.1, 0.6, str(res['hanya_B']), fontsize=13, weight='bold', color='#1B5E20')
        ax1.text(0.0, -1.2, str(res['hanya_C']), fontsize=13, weight='bold', color='#E65100')
        ax1.text(0.0, 0.95, str(res['hanya_AB']), fontsize=12, weight='bold')
        ax1.text(-0.55, -0.2, str(res['hanya_AC']), fontsize=12, weight='bold')
        ax1.text(0.55, -0.2, str(res['hanya_BC']), fontsize=12, weight='bold')
        ax1.text(0.0, 0.15, str(res['hanya_ABC']), fontsize=14, weight='bold', color='#B71C1C')
        ax1.text(1.5, -1.9, f"Luar = {res['di_luar']}", style='italic')
        ax1.set_title("Visualisasi Diagram Venn 3 Himpunan", weight='bold', pad=10)

        # Grafik Batang Distribusi
        labels = ['Hanya A', 'Hanya B', 'Hanya C', 'A & B', 'A & C', 'B & C', 'Ketiganya', 'Di Luar']
        vals = [res['hanya_A'], res['hanya_B'], res['hanya_C'], res['hanya_AB'], res['hanya_AC'], res['hanya_BC'], res['hanya_ABC'], res['di_luar']]
        ax2.barh(labels, vals, color=['#42A5F5', '#66BB6A', '#FFA726', '#AB47BC', '#26A69A', '#7E57C2', '#EF5350', '#78909C'])
        ax2.set_xlabel("Jumlah Entitas"); ax2.set_title("Segmentasi Wilayah Saling Lepas", weight='bold', pad=10)
        for i, v in enumerate(vals): ax2.text(v + 0.2, i, str(v), va='center', weight='bold')

        plt.tight_layout()
        plt.savefig(output_path, dpi=300)
        plt.close()
        print(f"[INFO] Gambar Diagram Venn disimpan di '{output_path}'")

# Fitur 5: Pengujian Otomatis pada 2 Dataset Contoh
if __name__ == "__main__":
    app = SistemKlasifikasiHimpunan()
    
    print("\n--- UJI DATASET 1: KEAHLIAN IT MAHASISWA ---")
    app.muat_dataset("data/dataset1_skill_mahasiswa.csv")
    d1 = app.hitung_inklusi_eksklusi("menguasai_python", "menguasai_java", "menguasai_sql")
    print(f"Hasil Rumus PIE: {d1['total_pie']} | Hasil Aktual: {d1['total_aktual']} -> Valid: {d1['valid']}")
    app.visualisasi_diagram_venn(d1, "output_venn_dataset1.png")

    print("\n--- UJI DATASET 2: MINAT KONSENTRASI STUDI ---")
    app.muat_dataset("data/dataset2_minat_studi.csv")
    d2 = app.hitung_inklusi_eksklusi("minat_ai", "minat_cybersecurity", "minat_webdev")
    print(f"Hasil Rumus PIE: {d2['total_pie']} | Hasil Aktual: {d2['total_aktual']} -> Valid: {d2['valid']}")
    app.visualisasi_diagram_venn(d2, "output_venn_dataset2.png")