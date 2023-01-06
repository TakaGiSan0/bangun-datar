import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar :
    selected = option_menu ("Perhitungan      Bangun Ruang",
    ["Pembukaan",
    "Perhitungan Persegi",
    "Perhitungan Persegi Panjang",
    "Perhitungan Segitiga",
    "Perhitungan Lingkaran"],
    defult_index=0)
    
if (selected == "Pembukaan") :
    st.write("""
    # Perkenalan
    Kami Ingin Hasil Kerja Sama Kami Dalam Pembuatan Aplikasi Perhitungan Sederhana Yang Beranggotakan :
    
    1. Muhamad Firdaus / 3312211069
    2. Andi Supri Anto / 3312211067
    3. Muhammad Deni Alqastha / 33122110
    4. Arjun Sidauruk / 33122110
    5. Joshua Christopher Sihombing / 3312211070
    """)
    
if (selected == "Perhitungan Persegi") :
    st.tittle("Perhitungan Luas Persegi")
    
    sisi = st.number_input ("Sisi", 0)
    hasil = st.button ("Hasil")
    
    if hasil :
        luas = sisi * sisi
        st.success (f"Luas Persegi Adalah = {luas}")
    
    st.tittle("Perhitungan Keliling Persegi")
    
    sisi = st.number_input ("Sisi", 0)
    hasil = st.button ("Hasil")
    
    if hasil :
        keliling = 4 * sisi
        st.success (f"Keliling Persegi Adalah = {keliling}")
        
if(selected == "Perhitungan Persegi Panjang") :
    st.tittle("Perhitungan Luas Persegi Panjang")
    
    panjang = st.number_input ("Panjang", 0)
    lebar = st.number_input ("Lebar", 0)
    hasil = st.button ("Hasil")
    
    if hasil :
        luas = panjang * lebar
        st.success (f"Luas Persegi Panjang Adalah = {luas}")
        
    st. tittle("Perhitungan Keliling Persegi Panjang")
    
    panjang = st.number_input ("Panjang", 0)
    lebar = st.number_input ("Lebar", 0)
    hasil = st.button("Hasil")
    
    if hasil :
        keliling = 2 * (panjang + lebar)
        st.success (f"Keliling Persegi Panjang Adalah = {keliling}")
        
if(selected == "Perhitungan Segitigas") :
    st.tittle("Perhitungan Luas Segitiga")
    
    alas = st.number_input ("Alas", 0)
    tinggi = st.number_input ("Tinggi", 0)
    hasil = st.button("Hasil")
    
    if hasil :
        luas = 0.5 * alas * tinggi
        st.success (f"Luas Segitiga Adalah = {luas}")
        
    st.tittle("Perhitungan Keliling Segitiga")
    
    sisi = st.number_input("Sisi", 0)
    hasil = st.button("Hasil")
    
    if hasil :
        keliling = sisi+sisi+sisi
        st.success(f"Keliling Segitiga Adalah = {keliling}")
        
if(selected == "Perhitungan Lingkaran") :
    st.tittle("Perhitungan Luas Lingkaran")
    
    jari = st.number_input("Jari-Jari", 0)
    hasil = st.button("Hasil")
    
    if hasil :
        luas = 3.14 * jari * jari
        st.success(f"Luas Lingkaran Adalah = {luas}")
        
    st.tiytle("Perhitungan Keliling Lingkaran")
    
    jari = st.number_input("Jari-Jari", 0)
    hasil = st.button("Hasil")
    
    if hasil :
        keliling = 2 * 3.14 * jari
        st.success(f"Keliling Lingkaran Adalah = {keliling}")