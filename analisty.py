import google.generativeai as genai
import os
import dotenv
import json

dotenv.load_dotenv()

class Analista():
    def __init__(self):
        print('Iniciando o Analista!')
        chave = os.getenv('GEMINAI_TOKEN')
        genai.configure(api_key=chave)
        self.model = genai.GenerativeModel('gemini-2.0-flash')
    

    def analisar(self,vaga,curriculo_texto):

        prompt = f'''
        Sua função é atuar como um Tech Recruiter Sênior e rígido.
            
        VAGA:
        {vaga}
        
        CURRÍCULO DO CANDIDATO:
        {curriculo_texto}
        
          Baseados em dados reais e informações atualizada, correlacione os dois e defina o nivel de conexão entre ambos. 

        SAÍDA OBRIGATÓRIA:
        Responda EXCLUSIVAMENTE em formato JSON (sem markdown, sem '```json'), seguindo esta estrutura exata:
        {{
            "match_score": (inteiro de 0 a 100),
            "pontos_fortes": ["ponto 1", "ponto 2", "ponto 3"],
            "pontos_fracos": ["ponto 1", "ponto 2", "ponto 3"],
            "conclusao_executiva": "texto curto e direto"
            "planejamento_futuro": "planejamento focado e direto"
        }}
        """'''
        
        print('Analista processando...')

        try:
            resposta = self.model.generate_content(prompt)
            text_limpo = resposta.text.replace("```json", "").replace("```", "").strip()
            resultado = json.loads(text_limpo)
            return resultado
        except Exception as e:
            print(f'Tivemos um erro cabuloso: {e}')
            
            return {"erro": f"Falha na análise: {e}"}
        
        

