import streamlit as st
import math

st.set_page_config(
    page_title="Aplikasi Perhitungan Luas Bangun Datar",page_icon="",)
st.title('Aplikasi Bangun Datar')
st.write("Silahkan pilih menu di samping untuk memulai")

def persegi(sisi):
    return sisi * sisi

menu=st.sidebar.selectbox('Pilih bangun datar', ['Luas Persegi', 'Luas Segitiga', 'Luas Lingkaran'])

if menu == 'Luas Persegi':
    st.header('Luas Persegi')

    st.image('https://www.rumusmatematika.com/wp-content/uploads/2018/02/rumus-luas-persegi-dan-keliling-persegi.jpg', caption="Rumus Luas Persegi", width=300)

    sisi = st.number_input('Masukkan panjang sisi persegi (cm):', min_value=0)
    if st.button('Hitung Luas Persegi'):
        luas = persegi(sisi)
        st.write(f'Luas Persegi dengan sisi {sisi} cm adalah {luas} cm²')

elif menu == 'Luas Segitiga':
    st.header('Luas Segitiga')

    st.image('https://www.rumusmatematika.com/wp-content/uploads/2018/02/rumus-luas-segitiga-dan-keliling-segitiga.jpg', caption="Rumus Luas Segitiga", width=300)

    alas = st.number_input('Masukkan panjang alas segitiga (cm):', min_value=0)
    tinggi = st.number_input('Masukkan tinggi segitiga (cm):', min_value=0)
    if st.button('Hitung Luas Segitiga'):
        luas = 0.5 * alas * tinggi
        st.write(f'Luas Segitiga dengan alas {alas} cm dan tinggi {tinggi} cm adalah {luas} cm²')

elif menu == 'Luas Lingkaran':
    st.header('Luas Lingkaran')

    st.image('https://www.nesamedia.com/wp-content/uploads/2020/06/rumus-luas-lingkaran.jpg', caption="Rumus Luas Lingkaran", width=300)

    jari_jari = st.number_input('Masukkan jari-jari lingkaran (cm):', min_value=0)
    if st.button('Hitung Luas Lingkaran'):
        luas = math.pi * jari_jari * jari_jari
        st.write(f'Luas Lingkaran dengan jari-jari {jari_jari} cm adalah {luas:.2f} cm²')