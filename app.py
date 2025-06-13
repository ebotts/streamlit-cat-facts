import streamlit as st
import requests

st.title("🐱 Random Cat Facts")

if st.button("Give me a cat fact!"):
    response = requests.get("https://catfact.ninja/fact")
    if response.status_code == 200:
        st.success(response.json()["fact"])
    else:
        st.error("Could not fetch a cat fact.")
