import streamlit as st

choice = st.sidebar.selectbox("select your choice",["Summarise Document"])

if choice == "Summarise Text":
    st.subheader("Summarise text using txtai")
    input_text=st.text_area("Enter you text here")
elif choice =="Summarise Document":
    st.subheader("Summarise Document using txtai")
