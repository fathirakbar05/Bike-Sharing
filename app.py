import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ===============================
# Konfigurasi Halaman
# ===============================
st.set_page_config(page_title="Dashboard Bike Sharing", layout="wide")

st.title("🚲 Dashboard Analisis Bike Sharing")
st.write("Visualisasi tren penggunaan sepeda berdasarkan waktu dan pengaruh cuaca.")

# ===============================
# Load Data
# ===============================
@st.cache_data
def load_data():
    return pd.read_csv("bike_clean.csv")

df = load_data()

# ===============================
# Preview Data
# ===============================
st.subheader("📄 Preview Dataset")
st.write("Menampilkan 5 baris pertama dari dataset setelah proses pembersihan data.")
st.dataframe(df.head())

# ===============================
# Ringkasan Statistik
# ===============================
st.subheader("📊 Ringkasan Statistik")
st.write(
    "Ringkasan statistik digunakan untuk memahami karakteristik dasar data, "
    "termasuk nilai minimum, maksimum, rata-rata, dan sebaran data."
)
st.dataframe(df.describe())


# ===============================
# PERBAIKAN BULAN (INI KUNCINYA)
# ===============================

# Jika mnth masih angka (1–12), ubah ke nama bulan
if df['mnth'].dtype != 'object':
    month_map = {
        1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr',
        5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug',
        9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
    }
    df['mnth'] = df['mnth'].map(month_map)

# Urutan bulan yang benar
month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

df['mnth'] = pd.Categorical(df['mnth'], categories=month_order, ordered=True)

# ===============================
# PERBAIKAN CUACA
# ===============================
weather_map = {
    1: 'Clear',
    2: 'Mist',
    3: 'Light Rain',
    4: 'Heavy Rain'
}

if df['weathersit'].dtype != 'object':
    df['weathersit'] = df['weathersit'].map(weather_map)

# Tahun
df['yr'] = df['yr'].astype(str)

# ===============================
# VISUALISASI
# ===============================
st.subheader("📈 Visualisasi Utama")

fig, axes = plt.subplots(1, 3, figsize=(20, 6))

# ===============================
# 1️⃣ Tren Bulanan (FIXED)
# ===============================
monthly_avg = df.groupby('mnth', observed=True)['cnt'].mean()

axes[0].plot(
    monthly_avg.index,
    monthly_avg.values,
    marker='o',
    linewidth=2
)
axes[0].set_title("Monthly Bike Rental Trend")
axes[0].set_xlabel("Month")
axes[0].set_ylabel("Average Rentals")
axes[0].tick_params(axis='x', rotation=45)

# ===============================
# 2️⃣ Tren Tahunan
# ===============================
yearly_avg = df.groupby('yr')['cnt'].mean()

axes[1].bar(
    yearly_avg.index,
    yearly_avg.values
)
axes[1].set_title("Yearly Bike Rental Trend")
axes[1].set_xlabel("Year")
axes[1].set_ylabel("Average Rentals")

# ===============================
# 3️⃣ Pengaruh Cuaca
# ===============================
weather_avg = df.groupby('weathersit')['cnt'].mean().sort_values(ascending=False)

axes[2].bar(
    weather_avg.index,
    weather_avg.values
)
axes[2].set_title("Impact of Weather on Bike Rentals")
axes[2].set_xlabel("Weather Condition")
axes[2].set_ylabel("Average Rentals")
axes[2].tick_params(axis='x', rotation=20)

plt.tight_layout()
st.pyplot(fig)

# ===============================
# INSIGHT
# ===============================
st.subheader("💡 Insight Utama")
st.markdown("""
1. **Tren bulanan menunjukkan pola musiman yang jelas**, di mana jumlah peminjaman sepeda cenderung meningkat pada bulan-bulan tertentu. Hal ini mengindikasikan bahwa faktor waktu dan musim berperan penting dalam memengaruhi tingkat penggunaan sepeda.

2. **Rata-rata peminjaman sepeda mengalami peningkatan dari tahun ke tahun**, yang menunjukkan adanya pertumbuhan minat masyarakat terhadap penggunaan sepeda, baik sebagai sarana transportasi maupun aktivitas rekreasi.

3. **Kondisi cuaca memiliki pengaruh signifikan terhadap jumlah peminjaman sepeda**. Cuaca cerah menghasilkan rata-rata peminjaman tertinggi, sedangkan cuaca buruk seperti hujan menyebabkan penurunan aktivitas peminjaman secara cukup drastis.
""")
st.markdown("---")
st.caption("🚲 Bike Sharing Dashboard | Muhammad Fathir Akbar – Teknik Informatika")
