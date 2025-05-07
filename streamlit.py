import streamlit as st

col1, col2 = st.columns([2, 3])

with col1:
    st.title("col1")

with col2:
    st.title("col2")

col1.subheader("sub header")
col2.checkbox("checkbox")



tab1, tab2 = st.tabs(["Tab A", "Tab B"])

with tab1:
    st.write("tab1")

with tab2:
    st.write("tab2")