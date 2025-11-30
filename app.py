import streamlit as st
from analisty import Analista




st.title('🎯 Job Hunter: O Analista de Vagas')
st.divider()

vaga = st.text_area('Cole a descrição da vaga aqui: ')
st.divider()

curriculo = st.text_area('Cole seu curriculo aqui: ')

if st.button('Analisar compatibilidade'):
    if not vaga or not curriculo:
        st.error("⚠️ Preencha a vaga e o currículo!")
    else:
        with st.spinner("🤖 O Agente está lendo..."):
            try:
                agente = Analista() 
                resposta = agente.analisar(vaga, curriculo)
                
                st.divider()
                st.write(resposta) 
                
            except Exception as e:
                st.error(f"Erro no sistema: {e}")
