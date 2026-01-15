import streamlit as st
import requests

st.title("Gerador de Tickets Azure DevOps")

type = st.selectbox("Tipo", ["feature", "bug"])
description = st.text_area("Descrição", height=150)

if st.button("Gerar Ticket"):
    if description.strip():
        with st.spinner("Gerando..."):
            try:
                response = requests.post(
                    "http://api:5454/generate-ticket",
                    json={
                        "type": type,
                        "description": description
                    },
                    timeout=60
                )
                
                if response.status_code == 200:
                    ticket = response.json().get("ticket", "").strip()
                    if ticket:
                        st.markdown(ticket)
                    else:
                        st.error("Ticket gerado está vazio")
                else:
                    error_msg = response.json().get("error", "Erro desconhecido")
                    st.error(f"Erro ao gerar ticket: {error_msg}")
                    
            except requests.exceptions.ConnectionError:
                st.error("Não foi possível conectar ao backend. Verifique se o serviço está rodando.")
            except requests.exceptions.Timeout:
                st.error("Tempo de espera esgotado. O modelo pode estar demorando muito para responder.")
            except requests.exceptions.RequestException as e:
                st.error(f"Erro na requisição: {str(e)}")
            except Exception as e:
                st.error(f"Erro inesperado: {str(e)}")
    else:
        st.warning("Preencha a descrição")
