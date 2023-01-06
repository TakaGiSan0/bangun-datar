import streamlit as st

# Using "with" notation
selected = st.sidebar.radio("Perhitungan Bangun Datar", ["Pembukaan", "Perhitungan Persegi", "Perhitungan Persegi Panjang", "Perhitungan Segitiga", "Perhitungan Lingkaran"])

if (selected == "Pembukaan") :
    st.write("""
    # Perkenalan
    Hari Ini Kami Ingin Menjelaskan Hasil Kerja Sama Kami Dalam Pembuatan Aplikasi Perhitungan Sederhana Yang Beranggotakan :
    
    1. Muhamad Firdaus / 3312211069
    2. Andi Supri Anto / 3312211067
    3. Muhammad Deni Alqastha / 3312211080
    4. Arjun Sidauruk / 3312211081
    5. Joshua Christoper Sihombing / 3312211070
    """)
    
if (selected == "Perhitungan Persegi") :
    st.title("Perhitungan Luas Persegi")
    
    sisi = st.number_input ("Sisi", 0)
    hasil = st.button ("Hasil")
    
    if hasil :
        luas = sisi * sisi
        st.success (f"Luas Persegi Adalah = {luas}")
    
    st.title("Perhitungan Keliling Persegi")
    
    s = st.number_input ("sisi", 0)
    hasil = st.button ("hasil")
    
    if hasil :
        keliling = 4 * s
        st.success (f"Keliling Persegi Adalah = {keliling}")
        
if(selected == "Perhitungan Persegi Panjang") :
    st.title("Perhitungan Luas Persegi Panjang")
    
    panjang = st.number_input ("Panjang", 0)
    lebar = st.number_input ("Lebar", 0)
    hasil = st.button ("Hasil")
    
    if hasil :
        luas = panjang * lebar
        st.success (f"Luas Persegi Panjang Adalah = {luas}")
        
    st. title("Perhitungan Keliling Persegi Panjang")
    
    panjang = st.number_input ("panjang", 0)
    lebar = st.number_input ("lebar", 0)
    hasil = st.button("hasil")
    
    if hasil :
        keliling = 2 * (panjang + lebar)
        st.success (f"Keliling Persegi Panjang Adalah = {keliling}")
        
if(selected == "Perhitungan Segitiga") :
    st.title("Perhitungan Luas Segitiga")
    
    alas = st.number_input ("Alas", 0)
    tinggi = st.number_input ("Tinggi", 0)
    hasil = st.button("Hasil")
    
    if hasil :
        luas = 0.5 * alas * tinggi
        st.success (f"Luas Segitiga Adalah = {luas}")
        
    st.title("Perhitungan Keliling Segitiga")
    
    sisi = st.number_input("Sisi", 0)
    hasil = st.button("hasil")
    
    if hasil :
        keliling = sisi+sisi+sisi
        st.success(f"Keliling Segitiga Adalah = {keliling}")
        
if(selected == "Perhitungan Lingkaran") :
    st.title("Perhitungan Luas Lingkaran")
    
    jari = st.number_input("Jari-Jari", 0)
    hasil = st.button("Hasil")
    
    if hasil :
        luas = 3.14 * jari * jari
        st.success(f"Luas Lingkaran Adalah = {luas}")
        
    st.title("Perhitungan Keliling Lingkaran")
    
    jari = st.number_input("jari-jari", 0)
    hasil = st.button("hasil")
    
    if hasil :
        keliling = 2 * 3.14 * jari
        st.success(f"Keliling Lingkaran Adalah = {keliling}")