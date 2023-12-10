import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Fungsi untuk memuat data
def load_data():
    data = pd.read_csv('mobil.csv')  # Ganti dengan path file data Anda
    return data

# Fungsi untuk melakukan analisis data
def analyze_data(data):
    # Tampilkan data tabel
    st.subheader('Data Tabel')
    st.dataframe(data)

    # Tampilkan informasi umum tentang data
    st.subheader('Informasi Data')
    st.write(f"Jumlah Baris: {data.shape[0]}")
    st.write(f"Jumlah Kolom: {data.shape[1]}")

    # Tampilkan statistik deskriptif
    st.subheader('Statistik Deskriptif')
    st.write(data.describe())

    # Visualisasi data
    st.subheader('Visualisasi Data')

    # Histogram
    st.write('Histogram')
    selected_column = st.selectbox('Pilih Kolom', data.columns)
    plt.figure(figsize=(8, 6))
    sns.histplot(data[selected_column].dropna(), kde=True)
    st.pyplot()

    # Scatter plot
    st.write('Scatter Plot')
    selected_x = st.selectbox('Pilih Kolom (sumbu x)', data.columns)
    selected_y = st.selectbox('Pilih Kolom (sumbu y)', data.columns)
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=data, x=selected_x, y=selected_y)
    st.pyplot()

# Main program
def main():
    st.title('Program Analisis Data')

    # Memuat data
    data = load_data()

    # Melakukan analisis data
    analyze_data(data)

# Menjalankan program
if __name__ == '__main__':
    main()
