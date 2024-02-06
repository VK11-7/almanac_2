import streamlit as st
from streamlit_gsheets import GSheetsConnection

url = 'https://docs.google.com/spreadsheets/d/1h2rVBV6X2gNg4hRNVFT26DoW-cbOnHEesF2oz9wipDo/edit?usp=sharing'

conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read(spreadsheets=url)

st.dataframe(df)
