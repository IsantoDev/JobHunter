import streamlit as st
from analisty import Analista
from pypdf import PdfReader




st.title('🎯 Job Hunter: O Analista de Vagas')
st.divider()

vaga = st.text_area('Cole a descrição da vaga aqui: ')
st.divider()

arquivo_pdf = st.file_uploader("📂 Envie seu Currículo (PDF)", type=["pdf"])
curriculo_texto = ""

if arquivo_pdf is not None:
    try:
        leitor = PdfReader(arquivo_pdf)
        for pagina in leitor.pages:
            curriculo_texto += pagina.extract_text()
        
        st.success("PDF carregado com sucesso!")
            
    except Exception as e:
        st.error(f"Erro ao ler PDF: {e}")

if st.button('Analisar compatibilidade'):

    if not vaga or not curriculo_texto:
        st.error("⚠️ Preencha a vaga e envie o PDF!")
    else:
        with st.spinner("🤖 O Agente está lendo e comparando os perfis..."):
            try:

                agente = Analista()
                

                resposta = agente.analisar(vaga, curriculo_texto)
                
            
                if "erro" in resposta:
                    st.error(resposta["erro"])
                else:
                    st.snow() 
                    score = resposta.get("match_score", 0)
                    
                    col_esq, col_dir = st.columns([1, 3])
                    with col_esq:
                        st.metric(label="Compatibilidade", value=f"{score}%")
                    with col_dir:
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
                st.error(f"Erro crítico no frontend: {e}")