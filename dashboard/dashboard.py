import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('data/day.csv')

st.header('Bicycle Rents Dashboard')

st.subheader('Dataframe of Bicycle Rents')
st.dataframe(data)

st.subheader("Pengaruh kondisi cuaca terhadap jumlah peminjaman sepeda melalui parameter temperature dan humidity")
st.write("Berdasarkan hasil analisis data, dapat disimpulkan bahwa terdapat pengaruh antara kondisi cuaca terhadap jumlah peminjaman sepeda. Hal ini dapat dilihat melalui scatter plot yang menunjukkan bahwa semakin tinggi temperature, jumlah peminjaman sepeda juga semakin tinggi. Sedangkan semakin tinggi humidity, jumlah peminjaman sepeda semakin rendah.")
tab1, tab2= st.tabs(["Temperatre", "Humidity"])
with tab1:
    plt.figure(figsize=(10, 5))
    sns.scatterplot(x='temp', y='cnt', data=data, )
    plt.title('Pengaruh Temperature Terhadap Jumlah Peminjaman Sepeda')
    plt.xlabel('Temperature')
    plt.ylabel('Jumlah Peminjaman Sepeda')
    st.pyplot(plt)

with tab2:
    plt.figure(figsize=(10, 5))
    sns.scatterplot(x='hum', y='cnt', data=data)
    plt.title('Pengaruh Humidity Terhadap Jumlah Peminjaman Sepeda')
    plt.xlabel('Humidity')
    plt.ylabel('Jumlah Peminjaman Sepeda')
    st.pyplot(plt)

st.subheader("perbedaan peminjaman sepeda antara hari kerja dan akhir pekan")
st.write("Berdasarkan hasil analisis data, dapat disimpulkan bahwa pada hari kerja terjadi peningkatan jumlah peminjaman sepeda dibandingkan dengan akhir pekan. Hal ini dapat dilihat melalui pie chart yang menunjukkan bahwa peminjaman sepeda pada hari kerja mencapai 69,62%.")

workingday_counts = data.groupby('workingday')['cnt'].sum()
labels = ['Akhir Pekan', 'Hari Kerja']
plt.figure(figsize=(3, 3))
plt.pie(workingday_counts, labels=labels, autopct='%1.2f%%')
plt.title('Perbedaan Peminjaman Sepeda antara Hari Kerja dan Akhir Pekan')
plt.axis('equal')
st.pyplot(plt)
