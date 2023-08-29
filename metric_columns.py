import streamlit as st

st.header("Periperal PC")
st.subheader("Minggu, 28 Agustus 2023")

st.metric(label="Harga Mouse", value="Rp. 1.000.000", delta="-Rp.150.000")
st.metric(label="Harga Keyboard", value="Rp. 1.500.000", delta="-Rp.350.000")
st.metric(label="Harga Headset", value="Rp. 650.000", delta="+Rp.250.000")
st.metric(label="Jumlah Barang", value="89", delta="89", delta_color="off")

st.write("---")

st.header("Taman Martani")
st.subheader("Minggu, 28 Agustus 2023")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="Suhu", value="34°C", delta="+2°C")
with col2:
    st.metric(label="Kelembapan", value="70%", delta="-6%")
with col3:
    st.metric(label="Tekanan", value="0,99atm", delta="-0,10atm")
with col4:
    st.metric(label="Peluang Hujan", value="2%", delta="+1%")

st.write("Dibuat oleh Muhammad Hanif Annafi ( 21537141009 )")