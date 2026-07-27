import streamlit as st
import requests

st.title("Pipo AI")

texto = st.text_area("Escreva seu texto:")

if st.button("Enviar"):
    response = requests.post(
        "http://34.175.145.133:8000/pipo",
        json={"texto": texto}
    )
    st.write("Resposta do Pipo:")
    st.json(response.json())
