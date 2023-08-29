import streamlit as st
import pandas as pd

data = {
    'Barang': ['Shampoo', 'Sabun', 'Pasta Gigi', 'Hand Sanitizer'],
    'Slot Tersedia': [15, 10, 8, 5],
    'Slot Terisi': [5, 8, 3, 2]
}
df = pd.DataFrame(data)

st.write("## Slot Barang Mini Market")
st.write(df)

col1, col2 = st.columns(2)

with col1:
    st.metric(label="Total Barang", value=df['Barang'].count())
with col2:
    st.metric(label="Total Slot Tersedia", value=df['Slot Tersedia'].sum())

st.write("Dibuat oleh Muhammad Hanif Annafi ( 21537141009 )")