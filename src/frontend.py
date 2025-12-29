import streamlit as st
import requests

st.title("Gerador de Tickets Azure DevOps")

type = st.selectbox("Tipo", ["feature", "bug"])
description = st.text_area("Descrição", height=150)

if st.button("Gerar Ticket"):
    if description.strip():
        with st.spinner("Gerando..."):
            response = requests.post("http://api:5454/generate-ticket", json={
                "type": type,
                "description": description
            })
            ticket = response.json().get("ticket", "").strip()
            st.markdown(ticket)
    else:
        st.warning("Preencha a descrição")
