import streamlit as st

st.title('🎯 Job Hunter: O Analista de Vagas')
st.divider()

vaga = st.text_area('Cole a descrição da vaga aqui: ')
st.divider()
st.text_area('Cole seu curriculo aqui: ')
st.button('Enviar')
