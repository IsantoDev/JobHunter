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
                
                st.snow() 
                score = resposta.get("match_score", 0)
                
          
                kpi1, kpi2 = st.columns([1, 3])
                with kpi1:
                    st.metric(label="Compatibilidade", value=f"{score}%")
                with kpi2:
                    st.write("Nível de Aderência à Vaga:")
                    st.progress(score)

                st.divider()
                col1, col2 = st.columns(2)
                
                with col1:
                    st.success("✅ Pontos Fortes")
                    for ponto in resposta.get("pontos_fortes", []):
                        st.write(f"• {ponto}")
                
                with col2:
                    st.error("⚠️ Pontos de Atenção")
                    for ponto in resposta.get("pontos_fracos", []):
                        st.write(f"• {ponto}")

                st.divider()
        
                st.subheader("💡 Conclusão do Recrutador")
                st.info(resposta.get("conclusao_executiva", "Sem conclusão."))
            
                if "planejamento_futuro" in resposta:
                    with st.expander("🚀 Ver Plano de Estudos Recomendado"):
                        st.write(resposta["planejamento_futuro"])
            
            except Exception as e:
                print(f'Deu bom não por esse erro aqui: {e}')