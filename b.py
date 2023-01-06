import streamlit as st

st.title("Perhitungan Luas Persegi")
    
sisi = st.number_input ("Sisi", 0)
hasil = st.button ("Hasil")
    
if hasil :
    luas = sisi * sisi
    st.success (f"Luas Persegi Adalah = {luas}")