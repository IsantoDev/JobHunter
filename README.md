# 🎯 Job Hunter AI

> **Seu Estrategista de Carreira Pessoal.** Uma aplicação baseada em IA que analisa a compatibilidade entre o seu Currículo e uma Vaga de Emprego.

## 💡 O Problema
Aplicar para vagas é exaustivo. Candidatos muitas vezes não sabem se seus currículos passam nos filtros de ATS (Sistemas de Rastreamento de Candidatos) ou se atendem aos requisitos específicos da vaga.

## 🛠️ A Solução
O **Job Hunter AI** utiliza Modelos de Linguagem (LLMs) para atuar como um Recrutador Técnico Sênior.
1.  **Entrada:** Cole a Descrição da Vaga + Envie seu Currículo (PDF).
2.  **Processamento:** O sistema extrai o texto usando `pypdf` e envia para o **Google Gemini** analisar via Engenharia de Prompt.
3.  **Saída:** Um relatório detalhado com Nota de Compatibilidade (0-100%), Pontos Fortes, Pontos a Melhorar e um Plano de Estudos.

## 🏗️ Stack Tecnológico
* **Frontend:** Streamlit (Interface Web em Python)
* **AI Core:** Google Gemini 1.5 Flash (via API)
* **Processamento de Dados:** PyPDF & Manipulação de JSON
* **Arquitetura:** Padrão desacoplado (Frontend e Backend separados)

## 🚀 Demo Online
[Clique aqui para acessar o App](https://jobhunteria.streamlit.app/)

---
*Desenvolvido por [Igor Santos](https://github.com/IsantoDev)*
