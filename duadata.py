import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Data mobil
car_data = pd.read_csv("mobil.csv")  # Ganti dengan path file data mobil Anda
st.header("Data Mobil")
st.dataframe(car_data)

# Data ritel
retail_data = pd.read_csv("dummy.csv")  # Ganti dengan path file data ritel Anda
st.header("Data Ritel")
st.dataframe(retail_data)

# Analisis data
st.header("Analisis Data")

# Tambahkan analisis data Anda di sini
# Misalnya, Anda bisa menggunakan grafik, metode statistik, atau visualisasi lainnya

# Contoh: Menampilkan grafik histogram dari harga mobil menggunakan matplotlib
st.subheader("Histogram Harga Mobil")
fig, ax = plt.subplots()
ax.hist(car_data["penjualan bulanan"])
st.pyplot(fig)

# Contoh: Menampilkan ringkasan statistik dari data ritel
st.subheader("Ringkasan Statistik Data Ritel")
st.write(retail_data.describe())

# Tambahkan analisis data tambahan sesuai kebutuhan Anda
