import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'Nama': ["Ghandy", "Hanif", "Aris", "Risky", "Uka"],
    'NIM': [1, 2, 3, 4, 5],
    'Universitas' : ["Poltek", "UNY", "UPI", "UMP", "Unej"]
})

df

st.write("Dibuat oleh Muhammad Hanif Annafi ( 21537141009 )")