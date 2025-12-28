Baik 👍
Berikut **isi README.md yang sudah lengkap, rapi, dan sesuai instruksi**, siap kamu **copy–paste langsung ke GitHub**.
Aku sesuaikan dengan **project Streamlit + analisis Bike Sharing** yang kamu buat.

---

# 🚲 Dashboard Analisis Bike Sharing

## 📌 Deskripsi Proyek

Proyek ini bertujuan untuk menganalisis **tren penggunaan sepeda** berdasarkan **waktu (bulanan dan tahunan)** serta **pengaruh kondisi cuaca** menggunakan dataset Bike Sharing.
Hasil analisis disajikan dalam bentuk **dashboard interaktif menggunakan Streamlit** agar mudah dipahami dan informatif.

---

## 📂 Dataset

Dataset yang digunakan adalah **Bike Sharing Dataset** yang akan melalui proses pembersihan data sebelum dipakai (`day.csv`).

**Beberapa atribut utama dalam dataset:**

1. `mnth` : Bulan
2. `yr` : Tahun
3. `cnt` : Jumlah total peminjaman sepeda
4. `weathersit` : Kondisi cuaca
5. Variabel pendukung lainnya terkait waktu dan lingkungan

---

## ▶️ Cara Menjalankan Proyek

### 1️⃣ Menjalankan Notebook (Opsional)

Jika ingin menjalankan analisis melalui notebook:

```bash
pip install -r requirements.txt
```

Kemudian buka file notebook:

```
ML_Muhammad_Fathir_Akbar.ipynb
```

---

### 2️⃣ Menjalankan Dashboard Streamlit (Wajib)

Pastikan sudah berada di direktori project, lalu jalankan perintah berikut:

```bash
pip install -r requirements.txt
streamlit run app.py
```

Jika berhasil, dashboard akan terbuka di browser pada:

```
http://localhost:8501
```

---

## 📊 Ringkasan Insight Analisis

1. **Tren penggunaan sepeda menunjukkan pola musiman yang jelas**, di mana jumlah peminjaman meningkat pada bulan-bulan tertentu. Hal ini mengindikasikan bahwa faktor waktu dan musim sangat memengaruhi aktivitas peminjaman sepeda.

2. **Rata-rata peminjaman sepeda mengalami peningkatan dari tahun ke tahun**, yang menunjukkan adanya pertumbuhan minat masyarakat terhadap penggunaan sepeda, baik sebagai sarana transportasi maupun aktivitas rekreasi.

3. **Kondisi cuaca memiliki pengaruh signifikan terhadap jumlah peminjaman sepeda**. Cuaca cerah menghasilkan tingkat peminjaman tertinggi, sedangkan cuaca buruk seperti hujan menyebabkan penurunan peminjaman secara cukup drastis.

---

## 🖼️ Screenshot Dashboard (Opsional)

Berikut tampilan dashboard hasil analisis:

![Dashboard Bike Sharing](Dashboard.png)

---

## 👤 Author

**Muhammad Fathir Akbar**
Program Studi Teknik Informatika
Fakultas Ilmu Komputer

---
