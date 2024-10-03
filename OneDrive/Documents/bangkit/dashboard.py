import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set_theme(style='dark')

# Memuat data
def load_data():
    # Ganti dengan jalur file Anda
    data = pd.read_csv('combined.csv')
    return data

# Memuat data
data = load_data()

# Judul Dashboard
st.title("Dashboard Kualitas Udara")

# Menampilkan Data
st.subheader("Data Kualitas Udara")
st.dataframe(data)

# Analisis Korelasi
st.subheader("Korelasi Antara PM2.5 dan Variabel Cuaca")
# Memilih hanya kolom numeric untuk analisis korelasi
columns_of_interest = ["PM2.5", "PM10", "SO2", "NO2", "CO", "O3", "TEMP", "PRES", "DEWP", "RAIN", "WSPM"]
correlation_data = data[columns_of_interest]
correlation = correlation_data.corr()

# Membuat heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
st.pyplot(plt)

# Menampilkan Grafik Per Kota
st.subheader("Pola Perubahan Konsentrasi PM2.5 per Kota")
cities = data['station'].unique()
selected_city = st.selectbox("Pilih Kota:", cities)

city_data = data[data['station'] == selected_city]
plt.figure(figsize=(10, 6))  # Ukuran grafik
sns.lineplot(data=city_data, x='year', y='PM2.5', marker='o')
plt.title(f'PM2.5 di {selected_city}')
plt.xlabel('Tahun')
plt.ylabel('Rata-rata Konsentrasi PM2.5')
st.pyplot(plt)

# Menampilkan Rata-rata PM2.5 per Stasiun untuk Tahun 2017
st.subheader("Rata-rata PM2.5 per Stasiun - Tahun 2017")

# Filter data untuk tahun 2017
year_2017_data = data[data['year'] == 2017]

# Menghitung rata-rata PM2.5 per stasiun
average_pollution_2017 = year_2017_data.groupby('station')['PM2.5'].mean().reset_index()

# Mengatur ukuran plot
plt.figure(figsize=(8, 6))
sns.barplot(data=average_pollution_2017, x='station', y='PM2.5')

plt.title('Rata-rata PM2.5 per Stasiun - Tahun 2017', fontsize=16)
plt.xlabel('Stasiun', fontsize=12)
plt.ylabel('Rata-rata PM2.5', fontsize=12)
plt.xticks(rotation=45)

# Menambahkan keterangan angka di atas setiap bar
for index, row in average_pollution_2017.iterrows():
    plt.text(index, row['PM2.5'] + 1, f'{row["PM2.5"]:.2f}', color='black', 
             ha='center', fontsize=10)

plt.tight_layout()
st.pyplot(plt)