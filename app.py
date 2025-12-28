import streamlit as st
import pandas as pd

# ===============================
# Konfigurasi Halaman
# ===============================
st.set_page_config(
    page_title="Dashboard Bike Sharing",
    layout="wide"
)

st.title("🚲 Dashboard Analisis Bike Sharing")
st.write("Dashboard ini menyajikan tren penggunaan sepeda berdasarkan waktu dan pengaruh kondisi cuaca.")

# ===============================
# Load Data
# ===============================
@st.cache_data
def load_data():
    return pd.read_csv("bike_clean.csv")

df = load_data()

# ===============================
# PREVIEW DATA
# ===============================
st.subheader("📄 Preview Dataset")
st.write("Menampilkan 5 baris pertama dataset.")
st.dataframe(df.head())

# ===============================
# RINGKASAN STATISTIK
# ===============================
st.subheader("📊 Ringkasan Statistik")
st.write("Ringkasan statistik memberikan gambaran awal karakteristik data numerik.")
st.dataframe(df.describe())

# ===============================
# PREPROCESSING
# ===============================

# Bulan (jika masih angka)
month_map = {
    1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr',
    5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug',
    9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
}

if df['mnth'].dtype != 'object':
    df['mnth'] = df['mnth'].map(month_map)

month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

df['mnth'] = pd.Categorical(df['mnth'], categories=month_order, ordered=True)

# Cuaca
weather_map = {
    1: 'Clear',
    2: 'Mist',
    3: 'Light Rain',
    4: 'Heavy Rain'
}

if df['weathersit'].dtype != 'object':
    df['weathersit'] = df['weathersit'].map(weather_map)

df['yr'] = df['yr'].astype(str)

# ===============================
# VISUALISASI UTAMA
# ===============================
st.subheader("📈 Visualisasi Utama")

col1, col2 = st.columns(2)

# Tren Bulanan
with col1:
    st.markdown("**Tren Penggunaan Sepeda Berdasarkan Bulan**")
    monthly_avg = df.groupby('mnth', observed=True)['cnt'].mean()
    st.line_chart(monthly_avg)

# Tren Tahunan
with col2:
    st.markdown("**Tren Penggunaan Sepeda Berdasarkan Tahun**")
    yearly_avg = df.groupby('yr')['cnt'].mean()
    st.bar_chart(yearly_avg)

# Pengaruh Cuaca
st.markdown("**Pengaruh Kondisi Cuaca terhadap Jumlah Peminjaman**")
weather_avg = df.groupby('weathersit')['cnt'].mean().sort_values(ascending=False)
st.bar_chart(weather_avg)

# ===============================
# INSIGHT
# ===============================
st.subheader("💡 Insight Utama")
st.markdown("""
1. **Tren bulanan menunjukkan pola musiman yang jelas**, di mana jumlah peminjaman sepeda meningkat pada bulan-bulan tertentu. Hal ini menandakan bahwa faktor waktu dan musim berpengaruh terhadap tingkat penggunaan sepeda.

2. **Terjadi peningkatan rata-rata peminjaman sepeda dari tahun ke tahun**, yang menunjukkan meningkatnya minat masyarakat terhadap penggunaan sepeda.

3. **Kondisi cuaca memiliki pengaruh signifikan terhadap peminjaman sepeda**, dengan cuaca cerah menghasilkan jumlah peminjaman tertinggi dibandingkan kondisi cuaca buruk.
""")

# ===============================
# FOOTER
# ===============================

st.markdown("---")

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown(
        """
        **🚲 Bike Sharing Dashboard**  
        Visualisasi Data Utama
        """
    )

with col2:
    st.markdown(
        """
        **Muhammad Fathir Akbar**  
        Teknik Informatika – Fakultas Ilmu Komputer
        """,
        unsafe_allow_html=True
    )

