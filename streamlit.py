import streamlit as st

col1, col2 = st.columns([2, 3])

with col1:
    st.title("col1")
with col2:
    st.title("col2")